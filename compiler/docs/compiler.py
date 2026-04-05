import ast
import os
import re
import shutil
from dataclasses import dataclass
from typing import Literal

HOME = "compiler/docs"
DESTINATION = "docs/source/telegram"
PYROGRAM_API_DEST = "docs/source/api"

FUNCTIONS_PATH = "pyrogram/raw/functions"
TYPES_PATH = "pyrogram/raw/types"
BASE_PATH = "pyrogram/raw/base"

FUNCTIONS_BASE = "functions"
TYPES_BASE = "types"
BASE_BASE = "base"

page_template = ""
toctree = ""


def snek(s: str):
    """Convert CamelCase to snake_case."""
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", s)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s).lower()


def get_title_list(s):
    """Parse a multi-line indented string into a list of stripped items."""
    return [i.strip() for i in [j.strip() for j in s.split("\n") if j] if i]


NodeType = Literal["class", "union"]


@dataclass
class NodeInfo:
    name: str
    type: NodeType


def _extract_union_name(node: ast.AST):
    """Extract the name of a variable that is assigned a Union type."""
    if isinstance(node, ast.Assign) and isinstance(node.value, ast.Subscript):
        if isinstance(node.value.value, ast.Name) and node.value.value.id == "Union":
            if isinstance(node.targets[0], ast.Name):
                return node.targets[0].id


def _extract_class_name(node: ast.AST):
    """Extract the name of a class."""
    if isinstance(node, ast.ClassDef):
        return node.name


def parse_node_info(node: ast.AST):
    """Parse an AST node and extract the class or variable name."""
    class_name = _extract_class_name(node)
    if class_name:
        return NodeInfo(name=class_name, type="class")
    union_name = _extract_union_name(node)
    if union_name:
        return NodeInfo(name=union_name, type="union")
    return None


def generate(source_path, base):
    """Auto-walk a raw API directory tree and generate RST docs for every class/union found."""
    all_entities = {}

    def build(path, level=0):
        last = path.split("/")[-1]

        for i in sorted(os.listdir(path)):
            try:
                if not i.startswith("__"):
                    build("/".join([path, i]), level=level + 1)
            except NotADirectoryError:
                with open(path + "/" + i, encoding="utf-8") as f:
                    try:
                        p = ast.parse(f.read())
                    except SyntaxError:
                        continue

                for node in ast.walk(p):
                    node_info = parse_node_info(node)
                    if node_info:
                        break
                else:
                    continue

                full_path = os.path.basename(path) + "/" + snek(node_info.name).replace("_", "-") + ".rst"

                if level:
                    full_path = base + "/" + full_path

                namespace = path.split("/")[-1]
                if namespace in ["base", "types", "functions"]:
                    namespace = ""

                full_name = f"{(namespace + '.') if namespace else ''}{node_info.name}"

                os.makedirs(os.path.dirname(DESTINATION + "/" + full_path), exist_ok=True)

                with open(DESTINATION + "/" + full_path, "w", encoding="utf-8") as f:
                    title_markup = "=" * len(full_name)
                    full_class_path = "pyrogram.raw.{}".format(
                        ".".join(full_path.split("/")[:-1]) + "." + node_info.name
                    )

                    if node_info.type == "class":
                        directive_type = "autoclass"
                        directive_suffix = "()"
                        directive_option = "members"
                    elif node_info.type == "union":
                        directive_type = "autodata"
                        directive_suffix = ""
                        directive_option = "annotation"
                    else:
                        raise ValueError(f"Unknown node type: `{node_info.type}`")

                    f.write(
                        page_template.format(
                            title=full_name,
                            title_markup=title_markup,
                            directive_type=directive_type,
                            full_class_path=full_class_path,
                            directive_suffix=directive_suffix,
                            directive_option=directive_option,
                        )
                    )

                if last not in all_entities:
                    all_entities[last] = []

                all_entities[last].append(node_info.name)

    build(source_path)

    for k, v in sorted(all_entities.items()):
        v = sorted(v)
        entities = []

        for i in v:
            entities.append(f'{i} <{snek(i).replace("_", "-")}>')

        if k != base:
            inner_path = base + "/" + k + "/index" + ".rst"
            module = "pyrogram.raw.{}.{}".format(base, k)
        else:
            for i in sorted(list(all_entities), reverse=True):
                if i != base:
                    entities.insert(0, "{0}/index".format(i))

            inner_path = base + "/index" + ".rst"
            module = "pyrogram.raw.{}".format(base)

        with open(DESTINATION + "/" + inner_path, "w", encoding="utf-8") as f:
            if k == base:
                f.write(":tocdepth: 1\n\n")
                k = "Raw " + k

            f.write(
                toctree.format(
                    title=k.title(),
                    title_markup="=" * len(k),
                    module=module,
                    entities="\n    ".join(entities)
                )
            )

            f.write("\n")


def _discover_methods(methods_root):
    """Auto-discover all Client methods from pyrogram/methods/ subdirectories.

    Returns a dict mapping category_key -> (display_name, [method_names]).
    """
    categories = {}
    dir_display_names = {
        "advanced": "Advanced",
        "auth": "Authorization",
        "bots": "Bots",
        "business": "Business",
        "chats": "Chats",
        "contacts": "Contacts",
        "decorators": "Decorators",
        "invite_links": "Invite Links",
        "messages": "Messages",
        "password": "Password",
        "payments": "Payments",
        "phone": "Phone",
        "pyromod": "Pyromod",
        "stickers": "Stickers",
        "users": "Users",
        "utilities": "Utilities",
    }

    for subdir in sorted(os.listdir(methods_root)):
        subdir_path = os.path.join(methods_root, subdir)
        if not os.path.isdir(subdir_path) or subdir.startswith("__"):
            continue
        methods = []
        for fname in sorted(os.listdir(subdir_path)):
            if fname.endswith(".py") and not fname.startswith("__"):
                methods.append(fname[:-3])
        if methods:
            display = dir_display_names.get(subdir, subdir.replace("_", " ").title())
            categories[subdir] = (display, methods)
    return categories


def _discover_types(types_root):
    """Auto-discover all pyrogram types from pyrogram/types/ subdirectories.

    Returns a dict mapping category_key -> (display_name, [class_names]).
    """
    dir_display_names = {
        "messages_and_media": "Messages & Media",
        "user_and_chats": "Users & Chats",
        "bots_and_keyboards": "Bot Keyboards",
        "inline_mode": "Inline Mode",
        "input_media": "Input Media",
        "input_message_content": "Input Message Content",
        "authorization": "Authorization",
        "payments": "Payments",
        "business": "Business",
        "pyromod": "Pyromod",
    }
    template_key_map = {
        "messages_and_media": "messages_media",
        "user_and_chats": "users_chats",
        "bots_and_keyboards": "bot_keyboards",
    }
    categories = {}
    for subdir in sorted(os.listdir(types_root)):
        subdir_path = os.path.join(types_root, subdir)
        if not os.path.isdir(subdir_path) or subdir.startswith("__"):
            continue
        classes = []
        for root, dirs, files in os.walk(subdir_path):
            for fname in sorted(files):
                if fname.endswith(".py") and not fname.startswith("__"):
                    fpath = os.path.join(root, fname)
                    with open(fpath, encoding="utf-8") as fh:
                        content = fh.read()
                    found = re.findall(r"^class\s+(\w+)\s*[\(:]", content, re.MULTILINE)
                    for c in found:
                        if not c.startswith("_"):
                            classes.append(c)
        if classes:
            key = template_key_map.get(subdir, subdir)
            display = dir_display_names.get(subdir, subdir.replace("_", " ").title())
            categories[key] = (display, sorted(set(classes)))
    return categories


def _discover_enums(enums_root):
    """Auto-discover all enumerations from pyrogram/enums/."""
    enums = []
    for fname in sorted(os.listdir(enums_root)):
        if fname.endswith(".py") and not fname.startswith("__"):
            fpath = os.path.join(enums_root, fname)
            with open(fpath, encoding="utf-8") as fh:
                content = fh.read()
            found = re.findall(r"^class\s+(\w+)\s*[\(:]", content, re.MULTILINE)
            for c in found:
                if not c.startswith("_") and c not in ("AutoName",):
                    enums.append(c)
    return sorted(set(enums))


def _generate_methods_template(categories):
    """Dynamically generate the methods index RST content."""
    lines = [
        "Available Methods",
        "=================",
        "",
        "All methods listed here are bound to a :class:`~pyrogram.Client` instance.",
        "",
        ".. code-block:: python",
        "",
        '    from pyrogram import Client',
        "",
        '    app = Client("my_account")',
        "",
        "    with app:",
        '        app.send_message(chat_id="me", text="Hi!")',
        "",
        "-----",
        "",
        ".. currentmodule:: pyrogram.Client",
        "",
    ]
    for key in categories:
        display, _ = categories[key]
        markup = "-" * len(display)
        lines.extend([
            display,
            markup,
            "",
            ".. autosummary::",
            "    :nosignatures:",
            "",
            "    {" + key + "_autosummary}",
            "",
            ".. toctree::",
            "    :hidden:",
            "",
            "    {" + key + "}",
            "",
        ])
    return "\n".join(lines)


def _generate_types_template(categories):
    """Dynamically generate the types index RST content."""
    lines = [
        "Available Types",
        "===============",
        "",
        "All types listed here are available through the ``pyrogram.types`` package.",
        "",
        ".. code-block:: python",
        "",
        "    from pyrogram.types import User, Message, ...",
        "",
        "-----",
        "",
        ".. currentmodule:: pyrogram.types",
        "",
    ]
    for key in categories:
        display, _ = categories[key]
        markup = "-" * len(display)
        lines.extend([
            display,
            markup,
            "",
            ".. autosummary::",
            "    :nosignatures:",
            "",
            "    {" + key + "}",
            "",
            ".. toctree::",
            "    :hidden:",
            "",
            "    {" + key + "}",
            "",
        ])
    return "\n".join(lines)


def pyrogram_api():
    """Generate high-level API docs: methods, types, enums, bound methods."""

    project_root = os.path.normpath(os.path.join(HOME, "../.."))
    methods_root = os.path.join(project_root, "pyrogram", "methods")
    types_root = os.path.join(project_root, "pyrogram", "types")
    enums_root = os.path.join(project_root, "pyrogram", "enums")

    method_categories = _discover_methods(methods_root)

    root = PYROGRAM_API_DEST + "/methods"
    shutil.rmtree(root, ignore_errors=True)
    os.mkdir(root)

    template_content = _generate_methods_template(method_categories)

    with open(root + "/index.rst", "w") as f:
        fmt_keys = {}
        for k, (display, methods) in method_categories.items():
            fmt_keys[k] = "\n    ".join("{0} <{0}>".format(m) for m in methods)
            fmt_keys[k + "_autosummary"] = "\n    ".join(methods)
            for method in methods:
                with open(root + "/{}.rst".format(method), "w") as f2:
                    title = "{}()".format(method)
                    f2.write(title + "\n" + "=" * len(title) + "\n\n")
                    if method in ("idle", "compose"):
                        f2.write(".. autofunction:: pyrogram.{}()".format(method))
                    else:
                        f2.write(".. automethod:: pyrogram.Client.{}()".format(method))
        f.write(template_content.format(**fmt_keys))

    type_categories = _discover_types(types_root)

    root = PYROGRAM_API_DEST + "/types"
    shutil.rmtree(root, ignore_errors=True)
    os.mkdir(root)

    template_content = _generate_types_template(type_categories)

    with open(root + "/index.rst", "w") as f:
        fmt_keys = {}
        for k, (display, types_list) in type_categories.items():
            fmt_keys[k] = "\n    ".join(types_list)
            for t in types_list:
                with open(root + "/{}.rst".format(t), "w") as f2:
                    title = "{}".format(t)
                    f2.write(title + "\n" + "=" * len(title) + "\n\n")
                    f2.write(".. autoclass:: pyrogram.types.{}()\n".format(t))
        f.write(template_content.format(**fmt_keys))

    enums = _discover_enums(enums_root)

    root = PYROGRAM_API_DEST + "/enums"
    shutil.rmtree(root, ignore_errors=True)
    os.mkdir(root)

    with open(root + "/cleanup.html", "w") as f:
        f.write("""<script>
  document
    .querySelectorAll("em.property")
    .forEach((elem, i) => i !== 0 ? elem.remove() : true)
  document
    .querySelectorAll("a.headerlink")
    .forEach((elem, i) => [0, 1].includes(i) ? true : elem.remove())
</script>""")

    enum_hlist = "\n    ".join("{}".format(e) for e in enums)
    enum_toctree = "\n    ".join("{}".format(e) for e in enums)

    with open(root + "/index.rst", "w") as f:
        f.write("Enumerations\n")
        f.write("============\n\n")
        f.write("All enumerations are available through the ``pyrogram.enums`` package.\n\n")
        f.write(".. code-block:: python\n\n")
        f.write("    from pyrogram.enums import ParseMode\n\n")
        f.write("-----\n\n")
        f.write(".. currentmodule:: pyrogram.enums\n\n")
        f.write("Enumerations\n")
        f.write("------------\n\n")
        f.write(".. autosummary::\n")
        f.write("    :nosignatures:\n\n")
        f.write("    " + enum_hlist + "\n\n")
        f.write(".. toctree::\n")
        f.write("    :hidden:\n\n")
        f.write("    " + enum_toctree + "\n")

    for enum in enums:
        with open(root + "/{}.rst".format(enum), "w") as f2:
            title = "{}".format(enum)
            f2.write(title + "\n" + "=" * len(title) + "\n\n")
            f2.write(".. autoclass:: pyrogram.enums.{}()\n".format(enum))
            f2.write("    :members:\n")
            f2.write("\n.. raw:: html\n    :file: ./cleanup.html\n")

    categories = dict(
        message="""
        Message
            Message.click
            Message.delete
            Message.download
            Message.forward
            Message.copy
            Message.pin
            Message.unpin
            Message.edit
            Message.edit_text
            Message.edit_caption
            Message.edit_media
            Message.edit_reply_markup
            Message.reply
            Message.reply_text
            Message.reply_animation
            Message.reply_audio
            Message.reply_cached_media
            Message.reply_chat_action
            Message.reply_contact
            Message.reply_document
            Message.reply_game
            Message.reply_inline_bot_result
            Message.reply_location
            Message.reply_media_group
            Message.reply_photo
            Message.reply_poll
            Message.reply_sticker
            Message.reply_venue
            Message.reply_video
            Message.reply_video_note
            Message.reply_voice
            Message.react
            Message.read
        """,
        chat="""
        Chat
            Chat.archive
            Chat.unarchive
            Chat.set_title
            Chat.set_description
            Chat.set_photo
            Chat.ban_member
            Chat.unban_member
            Chat.restrict_member
            Chat.promote_member
            Chat.get_member
            Chat.get_members
            Chat.add_members
            Chat.join
            Chat.leave
            Chat.mark_unread
            Chat.set_protected_content
            Chat.unpin_all_messages
        """,
        user="""
        User
            User.archive
            User.unarchive
            User.block
            User.unblock
        """,
        callback_query="""
        Callback Query
            CallbackQuery.answer
            CallbackQuery.edit_message_text
            CallbackQuery.edit_message_caption
            CallbackQuery.edit_message_media
            CallbackQuery.edit_message_reply_markup
            ChosenInlineResult.edit_message_text
            ChosenInlineResult.edit_message_caption
            ChosenInlineResult.edit_message_media
            ChosenInlineResult.edit_message_reply_markup
        """,
        inline_query="""
        InlineQuery
            InlineQuery.answer
        """,
        pre_checkout_query="""
        PreCheckoutQuery
            PreCheckoutQuery.answer
        """,
        shipping_query="""
        ShippingQuery
            ShippingQuery.answer
        """,
        chat_join_request="""
        ChatJoinRequest
            ChatJoinRequest.approve
            ChatJoinRequest.decline
        """,
        story="""
        Story
            Story.react
            Story.download
        """,
        active_session="""
        ActiveSession
            ActiveSession.terminate
        """,
    )

    root = PYROGRAM_API_DEST + "/bound-methods"
    shutil.rmtree(root, ignore_errors=True)
    os.mkdir(root)

    with open(HOME + "/template/bound-methods.rst") as f:
        template = f.read()

    with open(root + "/index.rst", "w") as f:
        fmt_keys = {}

        for k, v in categories.items():
            name, *bound_methods = get_title_list(v)
            fmt_keys.update({"{}_hlist".format(k): "\n    ".join("- :meth:`~{}`".format(bm) for bm in bound_methods)})
            fmt_keys.update({"{}_toctree".format(k): "\n    ".join("{} <{}>".format(bm.split(".")[-1], bm) for bm in bound_methods)})

            for bm in bound_methods:
                with open(root + "/{}.rst".format(bm), "w") as f2:
                    title = "{}()".format(bm)
                    f2.write(title + "\n" + "=" * len(title) + "\n\n")
                    f2.write(".. automethod:: pyrogram.types.{}()".format(bm))

        f.write(template.format(**fmt_keys))


def start():
    """Entry point: generate raw API docs + high-level API docs."""
    global page_template
    global toctree

    shutil.rmtree(DESTINATION, ignore_errors=True)

    with open(HOME + "/template/page.txt", encoding="utf-8") as f:
        page_template = f.read()

    with open(HOME + "/template/toctree.txt", encoding="utf-8") as f:
        toctree = f.read()

    generate(TYPES_PATH, TYPES_BASE)
    generate(FUNCTIONS_PATH, FUNCTIONS_BASE)
    generate(BASE_PATH, BASE_BASE)
    pyrogram_api()


if "__main__" == __name__:
    FUNCTIONS_PATH = "../../pyrogram/raw/functions"
    TYPES_PATH = "../../pyrogram/raw/types"
    BASE_PATH = "../../pyrogram/raw/base"
    HOME = "."
    DESTINATION = "../../docs/source/telegram"
    PYROGRAM_API_DEST = "../../docs/source/api"

    start()

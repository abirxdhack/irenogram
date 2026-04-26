import ast
import os
import re
import shutil
from dataclasses import dataclass
from typing import Literal

HOME = "compiler/docs"
DESTINATION = "docs/source/telegram"
IRENOGRAM_API_DEST = "docs/source/api"

FUNCTIONS_PATH = "pyrogram/raw/functions"
TYPES_PATH = "pyrogram/raw/types"
BASE_PATH = "pyrogram/raw/base"

FUNCTIONS_BASE = "functions"
TYPES_BASE = "types"
BASE_BASE = "base"

STANDALONE_METHODS = {"idle", "compose"}

INTERNAL_METHODS = {
    "decorator", "do_it", "get_chunk", "get_session", "make_input",
    "signal_handler", "worker", "count_populated_attributes", "callback",
    "check", "delete_waiter", "init", "markdown", "html", "link", "content",
    "forward_from", "forward_sender_name", "forward_from_chat",
    "forward_from_message_id", "forward_signature", "forward_date",
    "write", "read", "default", "full_name", "mention", "format",
    "stop_propagation", "continue_propagation", "matches", "count_populated",
}

BOUND_METHODS = {
    "add_members", "answer", "approve", "archive", "ban_member", "block",
    "click", "copy", "decline", "delete", "download",
    "edit", "edit_caption", "edit_media", "edit_reply_markup", "edit_text",
    "edit_message_text", "edit_message_caption", "edit_message_media",
    "edit_message_reply_markup",
    "export_link", "forward", "get_chat", "get_member", "get_members",
    "join", "leave", "mark_unread", "pin", "promote_member", "react", "read",
    "reply", "reply_animation", "reply_audio", "reply_cached_media",
    "reply_chat_action", "reply_contact", "reply_document", "reply_game",
    "reply_inline_bot_result", "reply_location", "reply_media_group",
    "reply_photo", "reply_poll", "reply_sticker", "reply_text", "reply_venue",
    "reply_video", "reply_video_note", "reply_voice", "reply_web_page",
    "restrict_member", "set_description", "set_photo", "set_protected_content",
    "set_title", "stop", "terminate", "unarchive", "unban_member", "unblock",
    "unpin", "unpin_all_messages",
}

toctree = ""


def snek(s: str):
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", s)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s).lower()


def get_title_list(s):
    return [i.strip() for i in [j.strip() for j in s.split("\n") if j] if i]


NodeType = Literal["class", "union"]


@dataclass
class NodeInfo:
    name: str
    type: NodeType


def _extract_union_name(node: ast.AST):
    if isinstance(node, ast.Assign) and isinstance(node.value, ast.Subscript):
        if isinstance(node.value.value, ast.Name) and node.value.value.id == "Union":
            if isinstance(node.targets[0], ast.Name):
                return node.targets[0].id


def _extract_class_name(node: ast.AST):
    if isinstance(node, ast.ClassDef):
        return node.name


def parse_node_info(node: ast.AST):
    class_name = _extract_class_name(node)
    if class_name:
        return NodeInfo(name=class_name, type="class")
    union_name = _extract_union_name(node)
    if union_name:
        return NodeInfo(name=union_name, type="union")
    return None


def _get_actual_method_name(filepath: str):
    try:
        with open(filepath, encoding="utf-8") as fh:
            src = fh.read()
        tree = ast.parse(src)
    except Exception:
        return None

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            name = node.name
            if not name.startswith("_") and name not in INTERNAL_METHODS:
                return name
    return None


def generate(source_path, base):
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

                    f.write(full_name + "\n")
                    f.write(title_markup + "\n\n")

                    if node_info.type == "class":
                        f.write(".. autoclass:: {}()\n".format(full_class_path))
                    elif node_info.type == "union":
                        f.write(".. autodata:: {}\n".format(full_class_path))
                        f.write("    :annotation:\n")
                    else:
                        raise ValueError("Unknown node type: `{}`".format(node_info.type))

                    f.write("\n")

                if last not in all_entities:
                    all_entities[last] = []

                all_entities[last].append(node_info.name)

    build(source_path)

    for k, v in sorted(all_entities.items()):
        v = sorted(v)
        entities = []

        for i in v:
            entities.append('{} <{}>'.format(i, snek(i).replace("_", "-")))

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


INTERNAL_CLASSES = {"Str", "Link", "Object", "AutoName"}


def _get_classes_from_dir(path):
    classes = []
    for root, dirs, files in os.walk(path):
        dirs[:] = sorted(d for d in dirs if not d.startswith("__"))
        for fname in sorted(files):
            if fname.endswith(".py") and not fname.startswith("__"):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath, encoding="utf-8") as fh:
                        content = fh.read()
                    tree = ast.parse(content)
                    for node in ast.walk(tree):
                        if isinstance(node, ast.ClassDef) and not node.name.startswith("_"):
                            if node.name not in INTERNAL_CLASSES:
                                classes.append(node.name)
                except Exception:
                    pass
    return sorted(set(classes))


def _discover_methods(methods_root):
    dir_display_names = {
        "account": "Account",
        "advanced": "Advanced",
        "auth": "Authorization",
        "bots": "Bots",
        "business": "Business",
        "chats": "Chats",
        "contacts": "Contacts",
        "invite_links": "Invite Links",
        "messages": "Messages",
        "password": "Password",
        "payments": "Payments",
        "phone": "Phone",
        "premium": "Premium",
        "pyromod": "Pyromod",
        "stickers": "Stickers",
        "stories": "Stories",
        "users": "Users",
        "utilities": "Utilities",
    }

    categories = {}
    seen_actual = set()
    subdir_order = [
        "account", "advanced", "auth", "bots", "business", "chats",
        "contacts", "invite_links", "messages", "password", "payments",
        "phone", "premium", "pyromod", "stickers", "stories", "users", "utilities",
    ]
    all_subdirs = sorted(os.listdir(methods_root))
    ordered = [s for s in subdir_order if s in all_subdirs] + \
              [s for s in all_subdirs if s not in subdir_order]
    for subdir in ordered:
        subdir_path = os.path.join(methods_root, subdir)
        if not os.path.isdir(subdir_path) or subdir.startswith("__") or subdir == "decorators":
            continue
        methods = []
        for fname in sorted(os.listdir(subdir_path)):
            if fname.endswith(".py") and not fname.startswith("__"):
                fpath = os.path.join(subdir_path, fname)
                actual_name = _get_actual_method_name(fpath)
                if actual_name and actual_name not in INTERNAL_METHODS and actual_name not in seen_actual:
                    methods.append((fname[:-3], actual_name))
                    seen_actual.add(actual_name)
        if methods:
            display = dir_display_names.get(subdir, subdir.replace("_", " ").title())
            categories[subdir] = (display, methods)
    return categories


def _discover_decorators(methods_root):
    decorators_path = os.path.join(methods_root, "decorators")
    decorators = []
    seen = set()
    if os.path.isdir(decorators_path):
        for fname in sorted(os.listdir(decorators_path)):
            if fname.endswith(".py") and not fname.startswith("__"):
                fpath = os.path.join(decorators_path, fname)
                actual_name = _get_actual_method_name(fpath)
                if actual_name and actual_name not in seen:
                    decorators.append((fname[:-3], actual_name))
                    seen.add(actual_name)
    return decorators


def _discover_types(types_root):
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
    seen_globally = set()
    for subdir in sorted(os.listdir(types_root)):
        subdir_path = os.path.join(types_root, subdir)
        if not os.path.isdir(subdir_path) or subdir.startswith("__"):
            continue
        all_classes = _get_classes_from_dir(subdir_path)
        classes = [c for c in all_classes if c not in seen_globally]
        seen_globally.update(classes)
        if classes:
            key = template_key_map.get(subdir, subdir)
            display = dir_display_names.get(subdir, subdir.replace("_", " ").title())
            categories[key] = (display, classes)
    return categories


def _discover_enums(enums_root):
    enums = []
    for fname in sorted(os.listdir(enums_root)):
        if fname.endswith(".py") and not fname.startswith("__"):
            fpath = os.path.join(enums_root, fname)
            try:
                with open(fpath, encoding="utf-8") as fh:
                    content = fh.read()
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        if not node.name.startswith("_") and node.name not in ("AutoName",):
                            enums.append(node.name)
            except Exception:
                found = re.findall(r"^class\s+(\w+)\s*[\(:]", content, re.MULTILINE)
                for c in found:
                    if not c.startswith("_") and c != "AutoName":
                        enums.append(c)
    return sorted(set(enums))


def _discover_handlers(handlers_root):
    handlers = []
    for fname in sorted(os.listdir(handlers_root)):
        if fname.endswith(".py") and not fname.startswith("__"):
            fpath = os.path.join(handlers_root, fname)
            try:
                with open(fpath, encoding="utf-8") as fh:
                    content = fh.read()
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef) and not node.name.startswith("_"):
                        if node.name != "Handler":
                            handlers.append(node.name)
            except Exception:
                pass
    return sorted(set(handlers))


def _write_method_rst(root, actual_method_name):
    rst_path = os.path.join(root, "{}.rst".format(actual_method_name))
    title = "{}()".format(actual_method_name)
    with open(rst_path, "w", encoding="utf-8") as f2:
        f2.write(title + "\n" + "=" * len(title) + "\n\n")
        if actual_method_name in STANDALONE_METHODS:
            f2.write(".. autofunction:: pyrogram.{}\n".format(actual_method_name))
        else:
            f2.write(".. automethod:: pyrogram.Client.{}()\n".format(actual_method_name))
        f2.write("\n")


def _write_type_rst(root, type_name):
    with open(os.path.join(root, "{}.rst".format(type_name)), "w", encoding="utf-8") as f2:
        title = "{}".format(type_name)
        f2.write(title + "\n" + "=" * len(title) + "\n\n")
        f2.write(".. autoclass:: pyrogram.types.{}()\n".format(type_name))
        f2.write("    :members:\n")
        f2.write("    :show-inheritance:\n")
        f2.write("\n")


def _generate_decorators_index(dest_root, decorators):
    idx_path = os.path.join(dest_root, "decorators", "index.rst")
    os.makedirs(os.path.dirname(idx_path), exist_ok=True)
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write("Decorators\n")
        f.write("==========\n\n")
        f.write("Decorators are used to register handlers on a :class:`~pyrogram.Client` instance.\n\n")
        f.write(".. hlist::\n")
        f.write("    :columns: 2\n\n")
        for _fname, actual in decorators:
            f.write("    * :doc:`{0}() <Client.{0}>`\n".format(actual))
        f.write("\n")
        f.write(".. toctree::\n")
        f.write("    :hidden:\n\n")
        for _fname, actual in decorators:
            f.write("    Client.{} <Client.{}>\n".format(actual, actual))
        f.write("\n")


def _generate_decorator_rst(dest_root, actual_method_name):
    dec_dir = os.path.join(dest_root, "decorators")
    os.makedirs(dec_dir, exist_ok=True)
    rst_name = "Client.{}.rst".format(actual_method_name)
    rst_path = os.path.join(dec_dir, rst_name)
    title = "Client.{}()".format(actual_method_name)
    with open(rst_path, "w", encoding="utf-8") as f:
        f.write(title + "\n" + "=" * len(title) + "\n\n")
        f.write(".. automethod:: pyrogram.Client.{}()\n\n".format(actual_method_name))


def _generate_handlers_index(dest_root, handlers):
    handlers_dir = os.path.join(dest_root, "handlers")
    os.makedirs(handlers_dir, exist_ok=True)
    idx_path = os.path.join(handlers_dir, "index.rst")
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write("Update Handlers\n")
        f.write("===============\n\n")
        f.write("Handlers are used with :meth:`~pyrogram.Client.add_handler` to process incoming updates.\n\n")
        f.write(".. currentmodule:: pyrogram.handlers\n\n")
        f.write(".. hlist::\n")
        f.write("    :columns: 2\n\n")
        for h in handlers:
            f.write("    * :class:`{}`\n".format(h))
        f.write("\n")
        f.write(".. toctree::\n")
        f.write("    :hidden:\n\n")
        for h in handlers:
            f.write("    {}\n".format(h))
        f.write("\n")
    for h in handlers:
        handler_path = os.path.join(handlers_dir, h + ".rst")
        with open(handler_path, "w", encoding="utf-8") as f:
            f.write(h + "\n")
            f.write("=" * len(h) + "\n\n")
            f.write(".. autoclass:: pyrogram.handlers." + h + "\n")
            f.write("    :members:\n")
            f.write("    :show-inheritance:\n")


def pyrogram_api():
    project_root = os.path.normpath(os.path.join(HOME, "../.."))
    methods_root = os.path.join(project_root, "pyrogram", "methods")
    types_root = os.path.join(project_root, "pyrogram", "types")
    enums_root = os.path.join(project_root, "pyrogram", "enums")
    handlers_root = os.path.join(project_root, "pyrogram", "handlers")

    method_categories = _discover_methods(methods_root)
    decorators = _discover_decorators(methods_root)
    handlers = _discover_handlers(handlers_root)

    root = IRENOGRAM_API_DEST + "/methods"
    shutil.rmtree(root, ignore_errors=True)
    os.makedirs(root, exist_ok=True)

    with open(root + "/index.rst", "w", encoding="utf-8") as f:
        lines = [
            "Available Methods",
            "=================",
            "",
            "All methods listed here are bound to a :class:`~pyrogram.Client` instance.",
            "",
            ".. code-block:: python",
            "",
            "    from pyrogram import Client",
            "",
            '    app = Client("my_account")',
            "",
            "    with app:",
            '        app.send_message(chat_id="me", text="Hi!")',
            "",
            "-----",
            "",
        ]

        for subdir, (display, methods) in method_categories.items():
            markup = "-" * len(display)
            lines += [display, markup, ""]
            lines += [".. hlist::", "    :columns: 3", ""]
            for _fname, actual in methods:
                lines.append("    * :doc:`{0}() <{0}>`".format(actual))
            lines.append("")
            lines += [".. toctree::", "    :hidden:", ""]
            lines.append(
                "    " + "\n    ".join(actual for _fname, actual in methods)
            )
            lines.append("")

            for _fname, actual in methods:
                _write_method_rst(root, actual)

        f.write("\n".join(lines))

    _generate_decorators_index(IRENOGRAM_API_DEST, decorators)
    for _fname, actual in decorators:
        _generate_decorator_rst(IRENOGRAM_API_DEST, actual)

    _generate_handlers_index(IRENOGRAM_API_DEST, handlers)

    type_categories = _discover_types(types_root)

    root = IRENOGRAM_API_DEST + "/types"
    shutil.rmtree(root, ignore_errors=True)
    os.makedirs(root, exist_ok=True)

    with open(root + "/index.rst", "w", encoding="utf-8") as f:
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

        for key, (display, types_list) in type_categories.items():
            markup = "-" * len(display)
            lines += [display, markup, ""]
            lines += [".. hlist::", "    :columns: 3", ""]
            lines.append("    " + "\n    ".join("* :doc:`{} <{}>`".format(t, t) for t in types_list))
            lines += ["", ".. toctree::", "    :hidden:", ""]
            lines.append("    " + "\n    ".join(types_list))
            lines.append("")

            for t in types_list:
                _write_type_rst(root, t)

        f.write("\n".join(lines))

    enums = _discover_enums(enums_root)

    root = IRENOGRAM_API_DEST + "/enums"
    shutil.rmtree(root, ignore_errors=True)
    os.makedirs(root, exist_ok=True)

    with open(root + "/cleanup.html", "w", encoding="utf-8") as f:
        f.write("""<script>
  document
    .querySelectorAll("em.property")
    .forEach((elem, i) => i !== 0 ? elem.remove() : true)
  document
    .querySelectorAll("a.headerlink")
    .forEach((elem, i) => [0, 1].includes(i) ? true : elem.remove())
</script>""")

    with open(root + "/index.rst", "w", encoding="utf-8") as f:
        f.write("Enumerations\n")
        f.write("============\n\n")
        f.write("All enumerations are available through the ``pyrogram.enums`` package.\n\n")
        f.write(".. code-block:: python\n\n")
        f.write("    from pyrogram.enums import ParseMode\n\n")
        f.write("-----\n\n")
        f.write(".. currentmodule:: pyrogram.enums\n\n")
        f.write("Enumerations\n")
        f.write("------------\n\n")
        f.write(".. hlist::\n")
        f.write("    :columns: 3\n\n")
        for enum in enums:
            f.write("    * :class:`{}`\n".format(enum))
        f.write("\n")
        f.write(".. toctree::\n")
        f.write("    :hidden:\n\n")
        f.write("    " + "\n    ".join(enums) + "\n")

    for enum in enums:
        with open(os.path.join(root, "{}.rst".format(enum)), "w", encoding="utf-8") as f2:
            title = "{}".format(enum)
            f2.write(title + "\n" + "=" * len(title) + "\n\n")
            f2.write(".. autoclass:: pyrogram.enums.{}()\n".format(enum))
            f2.write("    :members:\n")
            f2.write("    :undoc-members:\n")
            f2.write("    :show-inheritance:\n")
            f2.write("    :no-index:\n")

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
            Story.forward
            Story.export_link
        """,
        active_session="""
        ActiveSession
            ActiveSession.terminate
        """,
        poll="""
        Poll
            Poll.stop
        """,
        chat_member_updated="""
        ChatMemberUpdated
            ChatMemberUpdated.get_chat
            ChatMemberUpdated.get_member
        """,
    )

    root = IRENOGRAM_API_DEST + "/bound-methods"
    shutil.rmtree(root, ignore_errors=True)
    os.makedirs(root, exist_ok=True)

    with open(HOME + "/template/bound-methods.rst", encoding="utf-8") as f:
        template = f.read()

    with open(root + "/index.rst", "w", encoding="utf-8") as f:
        fmt_keys = {}

        for k, v in categories.items():
            name, *bound_methods = get_title_list(v)
            fmt_keys["{}_hlist".format(k)] = "\n    ".join(
                "- :doc:`{}() <{}>`".format(bm.split(".")[-1], bm) for bm in bound_methods
            )
            fmt_keys["{}_toctree".format(k)] = "\n    ".join(
                "{} <{}>".format(bm.split(".")[-1], bm) for bm in bound_methods
            )

            for bm in bound_methods:
                with open(os.path.join(root, "{}.rst".format(bm)), "w", encoding="utf-8") as f2:
                    title = "{}()".format(bm)
                    f2.write(title + "\n" + "=" * len(title) + "\n\n")
                    f2.write(".. automethod:: pyrogram.types.{}()\n".format(bm))

        try:
            f.write(template.format(**fmt_keys))
        except KeyError:
            content = template
            for key, val in fmt_keys.items():
                content = content.replace("{" + key + "}", val)
            f.write(content)


def start():
    global toctree

    shutil.rmtree(DESTINATION, ignore_errors=True)

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
    IRENOGRAM_API_DEST = "../../docs/source/api"

    start()
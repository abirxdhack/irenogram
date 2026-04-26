import os
import re
import sys
import types as _types

sys.path.insert(0, os.path.abspath("../.."))

try:
    import uvloop
except ImportError:
    uvloop = _types.ModuleType("uvloop")
    uvloop.EventLoopPolicy = type("EventLoopPolicy", (), {})
    sys.modules["uvloop"] = uvloop

with open(os.path.abspath("../../pyrogram/__init__.py"), encoding="utf-8") as _f:
    __version__ = re.search(
        r'^__version__\s*=\s*["\']([^"\']+)["\']',
        _f.read(), re.M
    ).group(1)

project = "Irenogram"
author = "Abir Arafat Chawdhury"
copyright = "2025, Abir Arafat Chawdhury"
release = __version__
version = __version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
]

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

master_doc = "index"
source_suffix = ".rst"
autodoc_member_order = "bysource"
autosummary_generate = True
autodoc_typehints = "none"

_CLIENT_EXCLUDE = (
    "APP_VERSION, DEVICE_MODEL, SYSTEM_VERSION, LANG_PACK, LANG_CODE, "
    "SYSTEM_LANG_CODE, PARENT_DIR, INVITE_LINK_RE, UPGRADED_GIFT_RE, "
    "SAVED_GIFT_RE, CHANNEL_MESSAGE_LINK_RE, WORKERS, WORKDIR, "
    "UPDATES_WATCHDOG_INTERVAL, MAX_CONCURRENT_TRANSMISSIONS, "
    "MAX_MESSAGE_CACHE_SIZE, MAX_TOPIC_CACHE_SIZE, mimetypes, "
    "loop, server_time, updates_watchdog, authorize, authorize_qr, "
    "fetch_peers, handle_updates, load_session, load_plugins, "
    "handle_download, get_file, get_dc_option, guess_mime_type, "
    "guess_extension, get_session, set_dc, set_parse_mode, "
    "read, write, default"
)

autodoc_default_options = {
    "undoc-members": False,
    "show-inheritance": True,
    "member-order": "bysource",
    "no-index": False,
    "exclude-members": _CLIENT_EXCLUDE,
}

autodoc_inherit_docstrings = True
autodoc_class_signature = "separated"

autodoc_mock_imports = [
    "cryptg",
    "tgcrypto",
    "bson",
    "pymongo",
    "qrcode",
    "python_socks",
]

templates_path = ["../resources/templates"]
html_copy_source = False
napoleon_use_rtype = False
napoleon_use_param = False
pygments_style = "sphinx"
pygments_dark_style = "monokai"
highlight_language = "python3"
copybutton_prompt_text = "$ "

suppress_warnings = [
    "image.not_readable",
    "ref.doc",
    "ref.any",
    "ref.meth",
    "ref.class",
    "ref.func",
    "ref.python",
    "toctree.excluded",
    "toctree.included",
    "toctree.not_included",
    "app.add_directive",
    "app.add_node",
    "duplicate",
    "docutils",
    "toc.not_included",
]

nitpicky = False
nitpick_ignore = [
    ("py:obj", "types"),
    ("py:class", "types"),
    ("py:func", "types"),
    ("py:meth", "types"),
    ("py:attr", "types"),
    ("py:class", "object"),
    ("py:class", "type"),
    ("py:obj", "object"),
]

html_title = f"Irenogram {version}"
html_theme = "furo"
html_static_path = [os.path.abspath("../../docs_static")]
html_css_files = ["irenogram.css"]
html_js_files = ["irenogram_docs.js"]
html_show_sourcelink = False
html_show_copyright = False
html_show_sphinx = False
html_logo = os.path.abspath("../../docs_static/irenogram.png")
html_favicon = os.path.abspath("../../docs_static/favicon.ico")

html_theme_options = {
    "navigation_with_keys": True,
    "sidebar_hide_name": True,
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/abirxdhack/irenogram",
            "html": (
                '<svg stroke="currentColor" fill="currentColor" stroke-width="0" '
                'viewBox="0 0 16 16" height="1em" width="1em" '
                'xmlns="http://www.w3.org/2000/svg">'
                '<path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59'
                '.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49'
                '-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53'
                '.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87'
                '.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15'
                '-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27'
                ' 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1'
                '.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65'
                ' 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15'
                '.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>'
                '</svg>'
            ),
            "class": "",
        },
    ],
}

html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/version.html",
        "sidebar/scroll-end.html",
    ]
}

html_baseurl = os.environ.get(
    "READTHEDOCS_CANONICAL_URL", "https://abirxdhack.github.io/irenogram/"
)


def _snek(s):
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", s)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s).lower().replace("_", "-")


def _target_to_url(target):
    base = html_baseurl.rstrip("/")

    m = re.match(r"^pyrogram\.Client\.(\w+)$", target)
    if m:
        return "{}/api/methods/{}/".format(base, m.group(1))

    m = re.match(r"^pyrogram\.types\.(\w+)$", target)
    if m:
        return "{}/api/types/{}/".format(base, m.group(1))

    m = re.match(r"^pyrogram\.enums\.(\w+)$", target)
    if m:
        return "{}/api/enums/{}/".format(base, m.group(1))

    m = re.match(r"^pyrogram\.filters\.(\w+)$", target)
    if m:
        return "{}/api/filters/".format(base)

    m = re.match(r"^pyrogram\.raw\.base\.(?:(\w+)\.)?(\w+)$", target)
    if m:
        ns, cls = m.group(1), m.group(2)
        if ns:
            return "{}/telegram/base/{}/{}/".format(base, _snek(ns), _snek(cls))
        return "{}/telegram/base/{}/".format(base, _snek(cls))

    m = re.match(r"^pyrogram\.raw\.types\.(?:(\w+)\.)?(\w+)$", target)
    if m:
        ns, cls = m.group(1), m.group(2)
        if ns:
            return "{}/telegram/types/{}/{}/".format(base, _snek(ns), _snek(cls))
        return "{}/telegram/types/{}/".format(base, _snek(cls))

    m = re.match(r"^pyrogram\.raw\.functions\.(?:(\w+)\.)?(\w+)$", target)
    if m:
        ns, cls = m.group(1), m.group(2)
        if ns:
            return "{}/telegram/functions/{}/{}/".format(base, _snek(ns), _snek(cls))
        return "{}/telegram/functions/{}/".format(base, _snek(cls))

    return None


def on_missing_reference(app, env, node, contnode):
    target = node.get("reftarget", "")
    if not target.startswith("pyrogram."):
        return None
    url = _target_to_url(target)
    if url is None:
        return None
    from docutils import nodes
    ref = nodes.reference("", "", internal=False, refuri=url)
    ref += contnode
    return ref


_SKIP_DUNDERS = {
    "__class__", "__delattr__", "__dict__", "__dir__", "__doc__",
    "__eq__", "__format__", "__ge__", "__getattribute__", "__getstate__",
    "__gt__", "__hash__", "__init_subclass__", "__le__", "__lt__",
    "__module__", "__ne__", "__new__", "__reduce__", "__reduce_ex__",
    "__repr__", "__setattr__", "__setstate__", "__sizeof__", "__str__",
    "__subclasshook__", "__weakref__", "__annotations__", "__abstractmethods__",
    "__slots__",
}
_SKIP_INTERNALS = {"read", "write", "default"}
_SKIP_CLASS_ATTRS = {"ID", "QUALNAME"}
_CLIENT_CONSTANTS = {
    "APP_VERSION", "DEVICE_MODEL", "SYSTEM_VERSION", "LANG_PACK", "LANG_CODE",
    "SYSTEM_LANG_CODE", "PARENT_DIR", "INVITE_LINK_RE", "UPGRADED_GIFT_RE",
    "SAVED_GIFT_RE", "CHANNEL_MESSAGE_LINK_RE", "WORKERS", "WORKDIR",
    "UPDATES_WATCHDOG_INTERVAL", "MAX_CONCURRENT_TRANSMISSIONS",
    "MAX_MESSAGE_CACHE_SIZE", "MAX_TOPIC_CACHE_SIZE", "mimetypes",
}
_CLIENT_INTERNALS = {
    "loop", "server_time", "updates_watchdog", "authorize", "authorize_qr",
    "fetch_peers", "handle_updates", "load_session", "load_plugins",
    "handle_download", "get_file", "get_dc_option", "guess_mime_type",
    "guess_extension", "get_session", "set_dc", "set_parse_mode",
}


def skip_member(app, what, name, obj, skip, options):
    if name in _SKIP_DUNDERS:
        return True
    if name in _SKIP_INTERNALS:
        return True
    if name in _SKIP_CLASS_ATTRS:
        return True
    if name in _CLIENT_CONSTANTS:
        return True
    if name in _CLIENT_INTERNALS:
        return True
    if name.endswith("_filter"):
        return True
    if name.startswith("_"):
        return True
    if skip:
        return True
    return False


def setup(app):
    app.connect("missing-reference", on_missing_reference)
    app.connect("autodoc-skip-member", skip_member)
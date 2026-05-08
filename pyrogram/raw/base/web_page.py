


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

WebPage = Union[raw.types.WebPage, raw.types.WebPageEmpty, raw.types.WebPageNotModified, raw.types.WebPagePending]


class WebPage:
    """Telegram API base type.

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            WebPage
            WebPageEmpty
            WebPageNotModified
            WebPagePending
    """

    QUALNAME = "pyrogram.raw.base.WebPage"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/web-page")

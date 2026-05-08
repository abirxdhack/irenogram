


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PageListItem = Union[raw.types.PageListItemBlocks, raw.types.PageListItemText]


class PageListItem:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PageListItemBlocks
            PageListItemText
    """

    QUALNAME = "pyrogram.raw.base.PageListItem"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/page-list-item")

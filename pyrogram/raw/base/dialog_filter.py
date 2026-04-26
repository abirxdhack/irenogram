


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

DialogFilter = Union[raw.types.DialogFilter, raw.types.DialogFilterChatlist, raw.types.DialogFilterDefault]


class DialogFilter:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            DialogFilter
            DialogFilterChatlist
            DialogFilterDefault
    """

    QUALNAME = "pyrogram.raw.base.DialogFilter"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/dialog-filter")

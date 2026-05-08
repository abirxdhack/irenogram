


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

QuickReply = Union[raw.types.QuickReply]


class QuickReply:
    """Telegram API base type.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            QuickReply
    """

    QUALNAME = "pyrogram.raw.base.QuickReply"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/quick-reply")

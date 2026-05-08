


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

AvailableReactions = Union[raw.types.messages.AvailableReactions, raw.types.messages.AvailableReactionsNotModified]


class AvailableReactions:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.AvailableReactions
            messages.AvailableReactionsNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAvailableReactions
    """

    QUALNAME = "pyrogram.raw.base.messages.AvailableReactions"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/available-reactions")

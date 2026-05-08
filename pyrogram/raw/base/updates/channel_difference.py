


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChannelDifference = Union[raw.types.updates.ChannelDifference, raw.types.updates.ChannelDifferenceEmpty, raw.types.updates.ChannelDifferenceTooLong]


class ChannelDifference:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            updates.ChannelDifference
            updates.ChannelDifferenceEmpty
            updates.ChannelDifferenceTooLong

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            updates.GetChannelDifference
    """

    QUALNAME = "pyrogram.raw.base.updates.ChannelDifference"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/channel-difference")

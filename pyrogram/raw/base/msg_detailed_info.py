


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MsgDetailedInfo = Union[raw.types.MsgDetailedInfo, raw.types.MsgNewDetailedInfo]


class MsgDetailedInfo:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            MsgDetailedInfo
            MsgNewDetailedInfo
    """

    QUALNAME = "pyrogram.raw.base.MsgDetailedInfo"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/msg-detailed-info")

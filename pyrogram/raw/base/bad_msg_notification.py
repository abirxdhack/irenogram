


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BadMsgNotification = Union[raw.types.BadMsgNotification, raw.types.BadServerSalt]


class BadMsgNotification:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            BadMsgNotification
            BadServerSalt
    """

    QUALNAME = "pyrogram.raw.base.BadMsgNotification"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/bad-msg-notification")

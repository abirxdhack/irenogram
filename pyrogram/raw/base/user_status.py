


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

UserStatus = Union[raw.types.UserStatusEmpty, raw.types.UserStatusLastMonth, raw.types.UserStatusLastWeek, raw.types.UserStatusOffline, raw.types.UserStatusOnline, raw.types.UserStatusRecently]


class UserStatus:
    """Telegram API base type.

    Constructors:
        This base type has 6 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            UserStatusEmpty
            UserStatusLastMonth
            UserStatusLastWeek
            UserStatusOffline
            UserStatusOnline
            UserStatusRecently
    """

    QUALNAME = "pyrogram.raw.base.UserStatus"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/user-status")

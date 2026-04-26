


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

User = Union[raw.types.User, raw.types.UserEmpty]


class User:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            User
            UserEmpty

    Functions:
        This object can be returned by 9 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.UpdateProfile
            account.UpdateUsername
            account.ChangePhone
            users.GetUsers
            contacts.ImportContactToken
            messages.GetFutureChatCreatorAfterLeave
            channels.GetMessageAuthor
            bots.GetAdminedBots
            bots.CreateBot
    """

    QUALNAME = "pyrogram.raw.base.User"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/user")

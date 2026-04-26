


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

LoginToken = Union[raw.types.auth.LoginToken, raw.types.auth.LoginTokenMigrateTo, raw.types.auth.LoginTokenSuccess]


class LoginToken:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            auth.LoginToken
            auth.LoginTokenMigrateTo
            auth.LoginTokenSuccess

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.ExportLoginToken
            auth.ImportLoginToken
    """

    QUALNAME = "pyrogram.raw.base.auth.LoginToken"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/login-token")

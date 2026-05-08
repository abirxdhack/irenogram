


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ResetPasswordResult = Union[raw.types.account.ResetPasswordFailedWait, raw.types.account.ResetPasswordOk, raw.types.account.ResetPasswordRequestedWait]


class ResetPasswordResult:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            account.ResetPasswordFailedWait
            account.ResetPasswordOk
            account.ResetPasswordRequestedWait

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.ResetPassword
    """

    QUALNAME = "pyrogram.raw.base.account.ResetPasswordResult"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/reset-password-result")

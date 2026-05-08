


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

EmailVerifyPurpose = Union[raw.types.EmailVerifyPurposeLoginChange, raw.types.EmailVerifyPurposeLoginSetup, raw.types.EmailVerifyPurposePassport]


class EmailVerifyPurpose:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            EmailVerifyPurposeLoginChange
            EmailVerifyPurposeLoginSetup
            EmailVerifyPurposePassport
    """

    QUALNAME = "pyrogram.raw.base.EmailVerifyPurpose"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/email-verify-purpose")

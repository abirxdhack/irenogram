


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PasskeyRegistrationOptions = Union[raw.types.account.PasskeyRegistrationOptions]


class PasskeyRegistrationOptions:
    """Telegram API base type.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            account.PasskeyRegistrationOptions

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.InitPasskeyRegistration
    """

    QUALNAME = "pyrogram.raw.base.account.PasskeyRegistrationOptions"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/passkey-registration-options")

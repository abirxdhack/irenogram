


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputPasskeyResponse = Union[raw.types.InputPasskeyResponseLogin, raw.types.InputPasskeyResponseRegister]


class InputPasskeyResponse:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputPasskeyResponseLogin
            InputPasskeyResponseRegister
    """

    QUALNAME = "pyrogram.raw.base.InputPasskeyResponse"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/input-passkey-response")

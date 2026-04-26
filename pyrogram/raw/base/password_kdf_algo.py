


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PasswordKdfAlgo = Union[raw.types.PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow, raw.types.PasswordKdfAlgoUnknown]


class PasswordKdfAlgo:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow
            PasswordKdfAlgoUnknown
    """

    QUALNAME = "pyrogram.raw.base.PasswordKdfAlgo"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/password-kdf-algo")

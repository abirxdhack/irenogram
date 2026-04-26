


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SecureRequiredType = Union[raw.types.SecureRequiredType, raw.types.SecureRequiredTypeOneOf]


class SecureRequiredType:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            SecureRequiredType
            SecureRequiredTypeOneOf
    """

    QUALNAME = "pyrogram.raw.base.SecureRequiredType"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/secure-required-type")




from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputCheckPasswordSRP = Union[raw.types.InputCheckPasswordEmpty, raw.types.InputCheckPasswordSRP]


class InputCheckPasswordSRP:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputCheckPasswordEmpty
            InputCheckPasswordSRP
    """

    QUALNAME = "pyrogram.raw.base.InputCheckPasswordSRP"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/input-check-password-srp")

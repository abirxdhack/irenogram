


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputUser = Union[raw.types.InputUser, raw.types.InputUserEmpty, raw.types.InputUserFromMessage, raw.types.InputUserSelf]


class InputUser:
    """Telegram API base type.

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputUser
            InputUserEmpty
            InputUserFromMessage
            InputUserSelf
    """

    QUALNAME = "pyrogram.raw.base.InputUser"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/input-user")

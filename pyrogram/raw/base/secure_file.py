


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SecureFile = Union[raw.types.SecureFile, raw.types.SecureFileEmpty]


class SecureFile:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            SecureFile
            SecureFileEmpty
    """

    QUALNAME = "pyrogram.raw.base.SecureFile"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/secure-file")

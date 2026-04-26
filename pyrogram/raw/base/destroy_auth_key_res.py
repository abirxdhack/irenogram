


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

DestroyAuthKeyRes = Union[raw.types.DestroyAuthKeyFail, raw.types.DestroyAuthKeyNone, raw.types.DestroyAuthKeyOk]


class DestroyAuthKeyRes:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            DestroyAuthKeyFail
            DestroyAuthKeyNone
            DestroyAuthKeyOk

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            DestroyAuthKey
    """

    QUALNAME = "pyrogram.raw.base.DestroyAuthKeyRes"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/destroy-auth-key-res")

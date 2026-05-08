


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ValidatedRequestedInfo = Union[raw.types.payments.ValidatedRequestedInfo]


class ValidatedRequestedInfo:
    """Telegram API base type.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            payments.ValidatedRequestedInfo

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.ValidateRequestedInfo
    """

    QUALNAME = "pyrogram.raw.base.payments.ValidatedRequestedInfo"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/validated-requested-info")

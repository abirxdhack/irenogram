


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

CodeType = Union[raw.types.auth.CodeTypeCall, raw.types.auth.CodeTypeFlashCall, raw.types.auth.CodeTypeFragmentSms, raw.types.auth.CodeTypeMissedCall, raw.types.auth.CodeTypeSms]


class CodeType:
    """Telegram API base type.

    Constructors:
        This base type has 5 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            auth.CodeTypeCall
            auth.CodeTypeFlashCall
            auth.CodeTypeFragmentSms
            auth.CodeTypeMissedCall
            auth.CodeTypeSms
    """

    QUALNAME = "pyrogram.raw.base.auth.CodeType"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/code-type")

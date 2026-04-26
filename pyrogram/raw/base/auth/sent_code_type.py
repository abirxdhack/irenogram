


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SentCodeType = Union[raw.types.auth.SentCodeTypeApp, raw.types.auth.SentCodeTypeCall, raw.types.auth.SentCodeTypeEmailCode, raw.types.auth.SentCodeTypeFirebaseSms, raw.types.auth.SentCodeTypeFlashCall, raw.types.auth.SentCodeTypeFragmentSms, raw.types.auth.SentCodeTypeMissedCall, raw.types.auth.SentCodeTypeSetUpEmailRequired, raw.types.auth.SentCodeTypeSms, raw.types.auth.SentCodeTypeSmsPhrase, raw.types.auth.SentCodeTypeSmsWord]


class SentCodeType:
    """Telegram API base type.

    Constructors:
        This base type has 11 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            auth.SentCodeTypeApp
            auth.SentCodeTypeCall
            auth.SentCodeTypeEmailCode
            auth.SentCodeTypeFirebaseSms
            auth.SentCodeTypeFlashCall
            auth.SentCodeTypeFragmentSms
            auth.SentCodeTypeMissedCall
            auth.SentCodeTypeSetUpEmailRequired
            auth.SentCodeTypeSms
            auth.SentCodeTypeSmsPhrase
            auth.SentCodeTypeSmsWord
    """

    QUALNAME = "pyrogram.raw.base.auth.SentCodeType"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/sent-code-type")

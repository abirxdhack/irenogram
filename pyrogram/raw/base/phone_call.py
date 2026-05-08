


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PhoneCall = Union[raw.types.PhoneCall, raw.types.PhoneCallAccepted, raw.types.PhoneCallDiscarded, raw.types.PhoneCallEmpty, raw.types.PhoneCallRequested, raw.types.PhoneCallWaiting]


class PhoneCall:
    """Telegram API base type.

    Constructors:
        This base type has 6 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PhoneCall
            PhoneCallAccepted
            PhoneCallDiscarded
            PhoneCallEmpty
            PhoneCallRequested
            PhoneCallWaiting
    """

    QUALNAME = "pyrogram.raw.base.PhoneCall"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/phone-call")

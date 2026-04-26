


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PaidReactionPrivacy = Union[raw.types.PaidReactionPrivacyAnonymous, raw.types.PaidReactionPrivacyDefault, raw.types.PaidReactionPrivacyPeer]


class PaidReactionPrivacy:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PaidReactionPrivacyAnonymous
            PaidReactionPrivacyDefault
            PaidReactionPrivacyPeer
    """

    QUALNAME = "pyrogram.raw.base.PaidReactionPrivacy"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/paid-reaction-privacy")

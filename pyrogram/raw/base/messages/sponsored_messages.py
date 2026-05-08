


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SponsoredMessages = Union[raw.types.messages.SponsoredMessages, raw.types.messages.SponsoredMessagesEmpty]


class SponsoredMessages:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.SponsoredMessages
            messages.SponsoredMessagesEmpty

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSponsoredMessages
    """

    QUALNAME = "pyrogram.raw.base.messages.SponsoredMessages"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/sponsored-messages")

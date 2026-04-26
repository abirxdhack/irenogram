


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

AffectedMessages = Union[raw.types.messages.AffectedMessages]


class AffectedMessages:
    """Telegram API base type.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.AffectedMessages

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.ReadHistory
            messages.DeleteMessages
            messages.ReadMessageContents
            channels.DeleteMessages
    """

    QUALNAME = "pyrogram.raw.base.messages.AffectedMessages"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/affected-messages")

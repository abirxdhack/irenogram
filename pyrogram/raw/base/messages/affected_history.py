


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

AffectedHistory = Union[raw.types.messages.AffectedHistory]


class AffectedHistory:
    """Telegram API base type.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.AffectedHistory

    Functions:
        This object can be returned by 8 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.DeleteHistory
            messages.ReadMentions
            messages.UnpinAllMessages
            messages.ReadReactions
            messages.DeleteSavedHistory
            messages.DeleteTopicHistory
            messages.ReadPollVotes
            channels.DeleteParticipantHistory
    """

    QUALNAME = "pyrogram.raw.base.messages.AffectedHistory"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/affected-history")

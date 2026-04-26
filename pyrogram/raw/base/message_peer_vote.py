


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MessagePeerVote = Union[raw.types.MessagePeerVote, raw.types.MessagePeerVoteInputOption, raw.types.MessagePeerVoteMultiple]


class MessagePeerVote:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            MessagePeerVote
            MessagePeerVoteInputOption
            MessagePeerVoteMultiple
    """

    QUALNAME = "pyrogram.raw.base.MessagePeerVote"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/message-peer-vote")

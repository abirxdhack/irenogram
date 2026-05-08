


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChatParticipant = Union[raw.types.ChatParticipant, raw.types.ChatParticipantAdmin, raw.types.ChatParticipantCreator]


class ChatParticipant:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ChatParticipant
            ChatParticipantAdmin
            ChatParticipantCreator
    """

    QUALNAME = "pyrogram.raw.base.ChatParticipant"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/chat-participant")

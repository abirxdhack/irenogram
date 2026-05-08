
from datetime import datetime

from pyrogram import enums, types

from .message_origin import MessageOrigin

class MessageOriginChat(MessageOrigin):
    """The message was originally sent on behalf of a chat to a group chat.


    Parameters:
        type (:obj:`~pyrogram.enums.MessageOriginType`):
            Type of the message origin.

        date (:py:obj:`~datetime.datetime`):
            Date the message was sent originally.

        sender_chat (:obj:`~pyrogram.types.Chat`):
            Chat that sent the message originally.

        author_signature (``str``, *optional*):
            For messages originally sent by an anonymous chat administrator, original message author signature.
    """
    def __init__(
        self,
        *,
        type: "enums.MessageOriginType" = enums.MessageOriginType.CHAT,
        date: datetime = None,
        sender_chat: "types.Chat" = None,
        author_signature: str = None
    ):
        super().__init__(
            type=type,
            date=date
        )

        self.sender_chat = sender_chat
        self.author_signature = author_signature

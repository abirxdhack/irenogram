
from datetime import datetime

from pyrogram import enums, types

from .message_origin import MessageOrigin

class MessageOriginChannel(MessageOrigin):
    """The message was originally sent to a channel chat.


    Parameters:
        type (:obj:`~pyrogram.enums.MessageOriginType`):
            Type of the message origin.

        date (:py:obj:`~datetime.datetime`):
            Date the message was sent originally.

        chat (:obj:`~pyrogram.types.Chat`):
            Channel chat to which the message was originally sent.

        message_id (``int``):
            Unique message identifier inside the chat.

        author_signature (``str``, *optional*):
            Signature of the original post author.
    """
    def __init__(
        self,
        *,
        type: "enums.MessageOriginType" = enums.MessageOriginType.CHANNEL,
        date: datetime = None,
        chat: "types.Chat" = None,
        message_id: int = None,
        author_signature: str = None
    ):
        super().__init__(
            type=type,
            date=date
        )

        self.chat = chat
        self.message_id = message_id
        self.author_signature = author_signature

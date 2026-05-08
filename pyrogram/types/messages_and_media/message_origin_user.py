
from datetime import datetime

from pyrogram import enums, types

from .message_origin import MessageOrigin

class MessageOriginUser(MessageOrigin):
    """The message was originally sent by a known user.


    Parameters:
        type (:obj:`~pyrogram.enums.MessageOriginType`):
            Type of the message origin.

        date (:py:obj:`~datetime.datetime`):
            Date the message was sent originally.

        sender_user (:obj:`~pyrogram.types.User`):
            User that sent the message originally.
    """
    def __init__(
        self,
        *,
        type: "enums.MessageOriginType" = enums.MessageOriginType.USER,
        date: datetime = None,
        sender_user: "types.User" = None
    ):
        super().__init__(
            type=type,
            date=date
        )

        self.sender_user = sender_user


from datetime import datetime

from pyrogram import enums

from .message_origin import MessageOrigin

class MessageOriginHiddenUser(MessageOrigin):
    """The message was originally sent by an unknown user.


    Parameters:
        type (:obj:`~pyrogram.enums.MessageOriginType`):
            Type of the message origin.

        date (:py:obj:`~datetime.datetime`):
            Date the message was sent originally.

        sender_user_name (``str``):
            Name of the user that sent the message originally.
    """
    def __init__(
        self,
        *,
        type: "enums.MessageOriginType" = enums.MessageOriginType.HIDDEN_USER,
        date: datetime = None,
        sender_user_name: str = None
    ):
        super().__init__(
            type=type,
            date=date
        )

        self.sender_user_name = sender_user_name

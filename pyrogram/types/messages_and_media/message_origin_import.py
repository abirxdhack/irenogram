
from datetime import datetime

from pyrogram import enums

from .message_origin import MessageOrigin

class MessageOriginImport(MessageOrigin):
    """Contains information about a message imported from a foreign chat service.


    Parameters:
        type (:obj:`~pyrogram.enums.MessageOriginType`):
            Type of the message origin.

        date (:py:obj:`~datetime.datetime`):
            Date the message was sent originally.

        sender_user_name (``str``):
            Name of the original sender.
    """
    def __init__(
        self,
        *,
        date: datetime = None,
        sender_user_name: str = None
    ):
        super().__init__(
            type=enums.MessageOriginType.IMPORT,
            date=date
        )

        self.sender_user_name = sender_user_name

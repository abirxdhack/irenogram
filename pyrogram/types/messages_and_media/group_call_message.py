
from datetime import datetime
from typing import Optional

import pyrogram
from pyrogram import raw, utils
from ..object import Object

class GroupCallMessage(Object):
    """A message sent inside a group call (live stream).


    Parameters:
        id (``int``): Message identifier within the call.
        from_id (``int`` | ``str``): Peer ID who sent the message.
        date (:py:obj:`~datetime.datetime`): When the message was sent.
        text (``str``): Message text.
        paid_message_stars (``int``, *optional*): Stars paid for a paid message.
        from_admin (``bool``, *optional*): True if sent by a call admin.
    """

    def __init__(self, *, client=None, id: int, from_id, date: datetime,
                 text: str, paid_message_stars: int = None, from_admin: bool = None):
        super().__init__(client)
        self.id = id
        self.from_id = from_id
        self.date = date
        self.text = text
        self.paid_message_stars = paid_message_stars
        self.from_admin = from_admin

    @staticmethod
    def _parse(client, msg: "raw.types.GroupCallMessage", users=None, chats=None) -> "GroupCallMessage":
        text = ""
        if getattr(msg, "message", None):
            text = msg.message.text if hasattr(msg.message, "text") else ""
        return GroupCallMessage(
            client=client,
            id=msg.id,
            from_id=msg.from_id,
            date=utils.timestamp_to_datetime(msg.date),
            text=text,
            paid_message_stars=getattr(msg, "paid_message_stars", None),
            from_admin=getattr(msg, "from_admin", None),
        )

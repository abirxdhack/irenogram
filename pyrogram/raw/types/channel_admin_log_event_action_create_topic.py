
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionCreateTopic(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``58707D28``

    Parameters:
        topic (:obj:`ForumTopic <pyrogram.raw.base.ForumTopic>`):
            N/A

    """

    __slots__: List[str] = ["topic"]

    ID = 0x58707d28
    QUALNAME = "types.ChannelAdminLogEventActionCreateTopic"

    def __init__(self, *, topic: "raw.base.ForumTopic") -> None:
        self.topic = topic

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionCreateTopic":
        
        topic = TLObject.read(b)
        
        return ChannelAdminLogEventActionCreateTopic(topic=topic)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.topic.write())
        
        return b.getvalue()

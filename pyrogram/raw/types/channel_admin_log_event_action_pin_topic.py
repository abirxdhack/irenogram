
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionPinTopic(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``5D8D353B``

    Parameters:
        prev_topic (:obj:`ForumTopic <pyrogram.raw.base.ForumTopic>`, *optional*):
            N/A

        new_topic (:obj:`ForumTopic <pyrogram.raw.base.ForumTopic>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["prev_topic", "new_topic"]

    ID = 0x5d8d353b
    QUALNAME = "types.ChannelAdminLogEventActionPinTopic"

    def __init__(self, *, prev_topic: "raw.base.ForumTopic" = None, new_topic: "raw.base.ForumTopic" = None) -> None:
        self.prev_topic = prev_topic
        self.new_topic = new_topic

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionPinTopic":
        
        flags = Int.read(b)
        
        prev_topic = TLObject.read(b) if flags & (1 << 0) else None
        
        new_topic = TLObject.read(b) if flags & (1 << 1) else None
        
        return ChannelAdminLogEventActionPinTopic(prev_topic=prev_topic, new_topic=new_topic)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.prev_topic is not None else 0
        flags |= (1 << 1) if self.new_topic is not None else 0
        b.write(Int(flags))
        
        if self.prev_topic is not None:
            b.write(self.prev_topic.write())
        
        if self.new_topic is not None:
            b.write(self.new_topic.write())
        
        return b.getvalue()

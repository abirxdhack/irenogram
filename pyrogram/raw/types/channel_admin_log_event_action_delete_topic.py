
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionDeleteTopic(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``AE168909``

    Parameters:
        topic (:obj:`ForumTopic <pyrogram.raw.base.ForumTopic>`):
            N/A

    """

    __slots__: List[str] = ["topic"]

    ID = 0xae168909
    QUALNAME = "types.ChannelAdminLogEventActionDeleteTopic"

    def __init__(self, *, topic: "raw.base.ForumTopic") -> None:
        self.topic = topic

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionDeleteTopic":
        
        topic = TLObject.read(b)
        
        return ChannelAdminLogEventActionDeleteTopic(topic=topic)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.topic.write())
        
        return b.getvalue()

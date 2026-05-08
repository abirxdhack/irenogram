
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdatePinnedChannelMessages(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``5BB98608``

    Parameters:
        channel_id (``int`` ``64-bit``):
            N/A

        messages (List of ``int`` ``32-bit``):
            N/A

        pts (``int`` ``32-bit``):
            N/A

        pts_count (``int`` ``32-bit``):
            N/A

        pinned (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["channel_id", "messages", "pts", "pts_count", "pinned"]

    ID = 0x5bb98608
    QUALNAME = "types.UpdatePinnedChannelMessages"

    def __init__(self, *, channel_id: int, messages: List[int], pts: int, pts_count: int, pinned: Optional[bool] = None) -> None:
        self.channel_id = channel_id
        self.messages = messages
        self.pts = pts
        self.pts_count = pts_count
        self.pinned = pinned

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePinnedChannelMessages":
        
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 0) else False
        channel_id = Long.read(b)
        
        messages = TLObject.read(b, Int)
        
        pts = Int.read(b)
        
        pts_count = Int.read(b)
        
        return UpdatePinnedChannelMessages(channel_id=channel_id, messages=messages, pts=pts, pts_count=pts_count, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pinned else 0
        b.write(Int(flags))
        
        b.write(Long(self.channel_id))
        
        b.write(Vector(self.messages, Int))
        
        b.write(Int(self.pts))
        
        b.write(Int(self.pts_count))
        
        return b.getvalue()

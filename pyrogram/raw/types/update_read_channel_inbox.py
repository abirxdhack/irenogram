
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateReadChannelInbox(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``922E6E10``

    Parameters:
        channel_id (``int`` ``64-bit``):
            N/A

        max_id (``int`` ``32-bit``):
            N/A

        still_unread_count (``int`` ``32-bit``):
            N/A

        pts (``int`` ``32-bit``):
            N/A

        folder_id (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["channel_id", "max_id", "still_unread_count", "pts", "folder_id"]

    ID = 0x922e6e10
    QUALNAME = "types.UpdateReadChannelInbox"

    def __init__(self, *, channel_id: int, max_id: int, still_unread_count: int, pts: int, folder_id: Optional[int] = None) -> None:
        self.channel_id = channel_id
        self.max_id = max_id
        self.still_unread_count = still_unread_count
        self.pts = pts
        self.folder_id = folder_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateReadChannelInbox":
        
        flags = Int.read(b)
        
        folder_id = Int.read(b) if flags & (1 << 0) else None
        channel_id = Long.read(b)
        
        max_id = Int.read(b)
        
        still_unread_count = Int.read(b)
        
        pts = Int.read(b)
        
        return UpdateReadChannelInbox(channel_id=channel_id, max_id=max_id, still_unread_count=still_unread_count, pts=pts, folder_id=folder_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.folder_id is not None else 0
        b.write(Int(flags))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        b.write(Long(self.channel_id))
        
        b.write(Int(self.max_id))
        
        b.write(Int(self.still_unread_count))
        
        b.write(Int(self.pts))
        
        return b.getvalue()

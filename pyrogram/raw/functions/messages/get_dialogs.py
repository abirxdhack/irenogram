
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetDialogs(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A0F4CB4F``

    Parameters:
        offset_date (``int`` ``32-bit``):
            N/A

        offset_id (``int`` ``32-bit``):
            N/A

        offset_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        hash (``int`` ``64-bit``):
            N/A

        exclude_pinned (``bool``, *optional*):
            N/A

        folder_id (``int`` ``32-bit``, *optional*):
            N/A

    Returns:
        :obj:`messages.Dialogs <pyrogram.raw.base.messages.Dialogs>`
    """

    __slots__: List[str] = ["offset_date", "offset_id", "offset_peer", "limit", "hash", "exclude_pinned", "folder_id"]

    ID = 0xa0f4cb4f
    QUALNAME = "functions.messages.GetDialogs"

    def __init__(self, *, offset_date: int, offset_id: int, offset_peer: "raw.base.InputPeer", limit: int, hash: int, exclude_pinned: Optional[bool] = None, folder_id: Optional[int] = None) -> None:
        self.offset_date = offset_date
        self.offset_id = offset_id
        self.offset_peer = offset_peer
        self.limit = limit
        self.hash = hash
        self.exclude_pinned = exclude_pinned
        self.folder_id = folder_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDialogs":
        
        flags = Int.read(b)
        
        exclude_pinned = True if flags & (1 << 0) else False
        folder_id = Int.read(b) if flags & (1 << 1) else None
        offset_date = Int.read(b)
        
        offset_id = Int.read(b)
        
        offset_peer = TLObject.read(b)
        
        limit = Int.read(b)
        
        hash = Long.read(b)
        
        return GetDialogs(offset_date=offset_date, offset_id=offset_id, offset_peer=offset_peer, limit=limit, hash=hash, exclude_pinned=exclude_pinned, folder_id=folder_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.exclude_pinned else 0
        flags |= (1 << 1) if self.folder_id is not None else 0
        b.write(Int(flags))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        b.write(Int(self.offset_date))
        
        b.write(Int(self.offset_id))
        
        b.write(self.offset_peer.write())
        
        b.write(Int(self.limit))
        
        b.write(Long(self.hash))
        
        return b.getvalue()

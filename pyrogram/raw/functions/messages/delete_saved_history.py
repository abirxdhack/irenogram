
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DeleteSavedHistory(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``4DC5085F``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        max_id (``int`` ``32-bit``):
            N/A

        parent_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

        min_date (``int`` ``32-bit``, *optional*):
            N/A

        max_date (``int`` ``32-bit``, *optional*):
            N/A

    Returns:
        :obj:`messages.AffectedHistory <pyrogram.raw.base.messages.AffectedHistory>`
    """

    __slots__: List[str] = ["peer", "max_id", "parent_peer", "min_date", "max_date"]

    ID = 0x4dc5085f
    QUALNAME = "functions.messages.DeleteSavedHistory"

    def __init__(self, *, peer: "raw.base.InputPeer", max_id: int, parent_peer: "raw.base.InputPeer" = None, min_date: Optional[int] = None, max_date: Optional[int] = None) -> None:
        self.peer = peer
        self.max_id = max_id
        self.parent_peer = parent_peer
        self.min_date = min_date
        self.max_date = max_date

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteSavedHistory":
        
        flags = Int.read(b)
        
        parent_peer = TLObject.read(b) if flags & (1 << 0) else None
        
        peer = TLObject.read(b)
        
        max_id = Int.read(b)
        
        min_date = Int.read(b) if flags & (1 << 2) else None
        max_date = Int.read(b) if flags & (1 << 3) else None
        return DeleteSavedHistory(peer=peer, max_id=max_id, parent_peer=parent_peer, min_date=min_date, max_date=max_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.parent_peer is not None else 0
        flags |= (1 << 2) if self.min_date is not None else 0
        flags |= (1 << 3) if self.max_date is not None else 0
        b.write(Int(flags))
        
        if self.parent_peer is not None:
            b.write(self.parent_peer.write())
        
        b.write(self.peer.write())
        
        b.write(Int(self.max_id))
        
        if self.min_date is not None:
            b.write(Int(self.min_date))
        
        if self.max_date is not None:
            b.write(Int(self.max_date))
        
        return b.getvalue()

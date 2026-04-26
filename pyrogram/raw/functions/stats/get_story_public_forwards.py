
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetStoryPublicForwards(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A6437EF6``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        id (``int`` ``32-bit``):
            N/A

        offset (``str``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`stats.PublicForwards <pyrogram.raw.base.stats.PublicForwards>`
    """

    __slots__: List[str] = ["peer", "id", "offset", "limit"]

    ID = 0xa6437ef6
    QUALNAME = "functions.stats.GetStoryPublicForwards"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, offset: str, limit: int) -> None:
        self.peer = peer
        self.id = id
        self.offset = offset
        self.limit = limit

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStoryPublicForwards":
        
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        offset = String.read(b)
        
        limit = Int.read(b)
        
        return GetStoryPublicForwards(peer=peer, id=id, offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        b.write(String(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()

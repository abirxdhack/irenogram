
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetPinnedStories(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``5821A5DC``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        offset_id (``int`` ``32-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`stories.Stories <pyrogram.raw.base.stories.Stories>`
    """

    __slots__: List[str] = ["peer", "offset_id", "limit"]

    ID = 0x5821a5dc
    QUALNAME = "functions.stories.GetPinnedStories"

    def __init__(self, *, peer: "raw.base.InputPeer", offset_id: int, limit: int) -> None:
        self.peer = peer
        self.offset_id = offset_id
        self.limit = limit

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPinnedStories":
        
        peer = TLObject.read(b)
        
        offset_id = Int.read(b)
        
        limit = Int.read(b)
        
        return GetPinnedStories(peer=peer, offset_id=offset_id, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()

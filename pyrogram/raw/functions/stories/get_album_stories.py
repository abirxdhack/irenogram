
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetAlbumStories(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``AC806D61``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        album_id (``int`` ``32-bit``):
            N/A

        offset (``int`` ``32-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`stories.Stories <pyrogram.raw.base.stories.Stories>`
    """

    __slots__: List[str] = ["peer", "album_id", "offset", "limit"]

    ID = 0xac806d61
    QUALNAME = "functions.stories.GetAlbumStories"

    def __init__(self, *, peer: "raw.base.InputPeer", album_id: int, offset: int, limit: int) -> None:
        self.peer = peer
        self.album_id = album_id
        self.offset = offset
        self.limit = limit

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAlbumStories":
        
        peer = TLObject.read(b)
        
        album_id = Int.read(b)
        
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        return GetAlbumStories(peer=peer, album_id=album_id, offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.album_id))
        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()

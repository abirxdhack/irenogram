
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class TopPeerCategoryPeers(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.TopPeerCategoryPeers`.

    Details:
        - Layer: ``224``
        - ID: ``FB834291``

    Parameters:
        category (:obj:`TopPeerCategory <pyrogram.raw.base.TopPeerCategory>`):
            N/A

        count (``int`` ``32-bit``):
            N/A

        peers (List of :obj:`TopPeer <pyrogram.raw.base.TopPeer>`):
            N/A

    """

    __slots__: List[str] = ["category", "count", "peers"]

    ID = 0xfb834291
    QUALNAME = "types.TopPeerCategoryPeers"

    def __init__(self, *, category: "raw.base.TopPeerCategory", count: int, peers: List["raw.base.TopPeer"]) -> None:
        self.category = category
        self.count = count
        self.peers = peers

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TopPeerCategoryPeers":
        
        category = TLObject.read(b)
        
        count = Int.read(b)
        
        peers = TLObject.read(b)
        
        return TopPeerCategoryPeers(category=category, count=count, peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.category.write())
        
        b.write(Int(self.count))
        
        b.write(Vector(self.peers))
        
        return b.getvalue()

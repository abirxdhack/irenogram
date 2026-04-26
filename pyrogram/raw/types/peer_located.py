
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PeerLocated(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PeerLocated`.

    Details:
        - Layer: ``224``
        - ID: ``CA461B5D``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        expires (``int`` ``32-bit``):
            N/A

        distance (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["peer", "expires", "distance"]

    ID = 0xca461b5d
    QUALNAME = "types.PeerLocated"

    def __init__(self, *, peer: "raw.base.Peer", expires: int, distance: int) -> None:
        self.peer = peer
        self.expires = expires
        self.distance = distance

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerLocated":
        
        peer = TLObject.read(b)
        
        expires = Int.read(b)
        
        distance = Int.read(b)
        
        return PeerLocated(peer=peer, expires=expires, distance=distance)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.expires))
        
        b.write(Int(self.distance))
        
        return b.getvalue()

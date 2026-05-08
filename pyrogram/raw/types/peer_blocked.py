
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PeerBlocked(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PeerBlocked`.

    Details:
        - Layer: ``224``
        - ID: ``E8FD8014``

    Parameters:
        peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        date (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["peer_id", "date"]

    ID = 0xe8fd8014
    QUALNAME = "types.PeerBlocked"

    def __init__(self, *, peer_id: "raw.base.Peer", date: int) -> None:
        self.peer_id = peer_id
        self.date = date

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerBlocked":
        
        peer_id = TLObject.read(b)
        
        date = Int.read(b)
        
        return PeerBlocked(peer_id=peer_id, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer_id.write())
        
        b.write(Int(self.date))
        
        return b.getvalue()

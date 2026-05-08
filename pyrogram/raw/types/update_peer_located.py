
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdatePeerLocated(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``B4AFCFB0``

    Parameters:
        peers (List of :obj:`PeerLocated <pyrogram.raw.base.PeerLocated>`):
            N/A

    """

    __slots__: List[str] = ["peers"]

    ID = 0xb4afcfb0
    QUALNAME = "types.UpdatePeerLocated"

    def __init__(self, *, peers: List["raw.base.PeerLocated"]) -> None:
        self.peers = peers

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePeerLocated":
        
        peers = TLObject.read(b)
        
        return UpdatePeerLocated(peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.peers))
        
        return b.getvalue()

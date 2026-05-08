
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StarsTransactionPeer(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarsTransactionPeer`.

    Details:
        - Layer: ``224``
        - ID: ``D80DA15D``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

    """

    __slots__: List[str] = ["peer"]

    ID = 0xd80da15d
    QUALNAME = "types.StarsTransactionPeer"

    def __init__(self, *, peer: "raw.base.Peer") -> None:
        self.peer = peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsTransactionPeer":
        
        peer = TLObject.read(b)
        
        return StarsTransactionPeer(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        return b.getvalue()

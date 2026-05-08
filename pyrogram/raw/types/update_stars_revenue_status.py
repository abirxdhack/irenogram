
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateStarsRevenueStatus(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``A584B019``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        status (:obj:`StarsRevenueStatus <pyrogram.raw.base.StarsRevenueStatus>`):
            N/A

    """

    __slots__: List[str] = ["peer", "status"]

    ID = 0xa584b019
    QUALNAME = "types.UpdateStarsRevenueStatus"

    def __init__(self, *, peer: "raw.base.Peer", status: "raw.base.StarsRevenueStatus") -> None:
        self.peer = peer
        self.status = status

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStarsRevenueStatus":
        
        peer = TLObject.read(b)
        
        status = TLObject.read(b)
        
        return UpdateStarsRevenueStatus(peer=peer, status=status)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(self.status.write())
        
        return b.getvalue()

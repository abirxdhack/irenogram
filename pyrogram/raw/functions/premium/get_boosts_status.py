
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetBoostsStatus(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``42F1F61``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    Returns:
        :obj:`premium.BoostsStatus <pyrogram.raw.base.premium.BoostsStatus>`
    """

    __slots__: List[str] = ["peer"]

    ID = 0x42f1f61
    QUALNAME = "functions.premium.GetBoostsStatus"

    def __init__(self, *, peer: "raw.base.InputPeer") -> None:
        self.peer = peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBoostsStatus":
        
        peer = TLObject.read(b)
        
        return GetBoostsStatus(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        return b.getvalue()

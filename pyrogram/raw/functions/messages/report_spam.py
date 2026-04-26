
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReportSpam(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``CF1592DB``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer"]

    ID = 0xcf1592db
    QUALNAME = "functions.messages.ReportSpam"

    def __init__(self, *, peer: "raw.base.InputPeer") -> None:
        self.peer = peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportSpam":
        
        peer = TLObject.read(b)
        
        return ReportSpam(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        return b.getvalue()

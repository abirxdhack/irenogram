
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetHistoryTTL(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``B80E5FE4``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        period (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "period"]

    ID = 0xb80e5fe4
    QUALNAME = "functions.messages.SetHistoryTTL"

    def __init__(self, *, peer: "raw.base.InputPeer", period: int) -> None:
        self.peer = peer
        self.period = period

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetHistoryTTL":
        
        peer = TLObject.read(b)
        
        period = Int.read(b)
        
        return SetHistoryTTL(peer=peer, period=period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.period))
        
        return b.getvalue()

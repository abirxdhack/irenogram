
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PaidReactionPrivacyPeer(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PaidReactionPrivacy`.

    Details:
        - Layer: ``224``
        - ID: ``DC6CFCF0``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    """

    __slots__: List[str] = ["peer"]

    ID = 0xdc6cfcf0
    QUALNAME = "types.PaidReactionPrivacyPeer"

    def __init__(self, *, peer: "raw.base.InputPeer") -> None:
        self.peer = peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaidReactionPrivacyPeer":
        
        peer = TLObject.read(b)
        
        return PaidReactionPrivacyPeer(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        return b.getvalue()

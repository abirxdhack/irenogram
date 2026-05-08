
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReportEncryptedSpam(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``4B0C8C0F``

    Parameters:
        peer (:obj:`InputEncryptedChat <pyrogram.raw.base.InputEncryptedChat>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer"]

    ID = 0x4b0c8c0f
    QUALNAME = "functions.messages.ReportEncryptedSpam"

    def __init__(self, *, peer: "raw.base.InputEncryptedChat") -> None:
        self.peer = peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportEncryptedSpam":
        
        peer = TLObject.read(b)
        
        return ReportEncryptedSpam(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        return b.getvalue()

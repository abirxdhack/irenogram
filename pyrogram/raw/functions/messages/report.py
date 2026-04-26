
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class Report(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``FC78AF9B``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        id (List of ``int`` ``32-bit``):
            N/A

        option (``bytes``):
            N/A

        message (``str``):
            N/A

    Returns:
        :obj:`ReportResult <pyrogram.raw.base.ReportResult>`
    """

    __slots__: List[str] = ["peer", "id", "option", "message"]

    ID = 0xfc78af9b
    QUALNAME = "functions.messages.Report"

    def __init__(self, *, peer: "raw.base.InputPeer", id: List[int], option: bytes, message: str) -> None:
        self.peer = peer
        self.id = id
        self.option = option
        self.message = message

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Report":
        
        peer = TLObject.read(b)
        
        id = TLObject.read(b, Int)
        
        option = Bytes.read(b)
        
        message = String.read(b)
        
        return Report(peer=peer, id=id, option=option, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Vector(self.id, Int))
        
        b.write(Bytes(self.option))
        
        b.write(String(self.message))
        
        return b.getvalue()

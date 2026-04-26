
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetFactCheck(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``B9CDC5EE``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        msg_id (List of ``int`` ``32-bit``):
            N/A

    Returns:
        List of :obj:`FactCheck <pyrogram.raw.base.FactCheck>`
    """

    __slots__: List[str] = ["peer", "msg_id"]

    ID = 0xb9cdc5ee
    QUALNAME = "functions.messages.GetFactCheck"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: List[int]) -> None:
        self.peer = peer
        self.msg_id = msg_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFactCheck":
        
        peer = TLObject.read(b)
        
        msg_id = TLObject.read(b, Int)
        
        return GetFactCheck(peer=peer, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Vector(self.msg_id, Int))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetMessagesReactions(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``8BBA90E6``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        id (List of ``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "id"]

    ID = 0x8bba90e6
    QUALNAME = "functions.messages.GetMessagesReactions"

    def __init__(self, *, peer: "raw.base.InputPeer", id: List[int]) -> None:
        self.peer = peer
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessagesReactions":
        
        peer = TLObject.read(b)
        
        id = TLObject.read(b, Int)
        
        return GetMessagesReactions(peer=peer, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Vector(self.id, Int))
        
        return b.getvalue()

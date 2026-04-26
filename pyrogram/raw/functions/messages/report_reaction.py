
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReportReaction(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``3F64C076``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        id (``int`` ``32-bit``):
            N/A

        reaction_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "id", "reaction_peer"]

    ID = 0x3f64c076
    QUALNAME = "functions.messages.ReportReaction"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, reaction_peer: "raw.base.InputPeer") -> None:
        self.peer = peer
        self.id = id
        self.reaction_peer = reaction_peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportReaction":
        
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        reaction_peer = TLObject.read(b)
        
        return ReportReaction(peer=peer, id=id, reaction_peer=reaction_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        b.write(self.reaction_peer.write())
        
        return b.getvalue()

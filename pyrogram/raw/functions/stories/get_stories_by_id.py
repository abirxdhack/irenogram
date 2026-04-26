
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetStoriesByID(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``5774CA74``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        id (List of ``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`stories.Stories <pyrogram.raw.base.stories.Stories>`
    """

    __slots__: List[str] = ["peer", "id"]

    ID = 0x5774ca74
    QUALNAME = "functions.stories.GetStoriesByID"

    def __init__(self, *, peer: "raw.base.InputPeer", id: List[int]) -> None:
        self.peer = peer
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStoriesByID":
        
        peer = TLObject.read(b)
        
        id = TLObject.read(b, Int)
        
        return GetStoriesByID(peer=peer, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Vector(self.id, Int))
        
        return b.getvalue()

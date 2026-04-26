
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DeleteStarGiftCollection(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``AD5648E8``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        collection_id (``int`` ``32-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "collection_id"]

    ID = 0xad5648e8
    QUALNAME = "functions.payments.DeleteStarGiftCollection"

    def __init__(self, *, peer: "raw.base.InputPeer", collection_id: int) -> None:
        self.peer = peer
        self.collection_id = collection_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteStarGiftCollection":
        
        peer = TLObject.read(b)
        
        collection_id = Int.read(b)
        
        return DeleteStarGiftCollection(peer=peer, collection_id=collection_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.collection_id))
        
        return b.getvalue()

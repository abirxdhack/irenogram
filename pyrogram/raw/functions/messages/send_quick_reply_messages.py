
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SendQuickReplyMessages(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``6C750DE1``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        shortcut_id (``int`` ``32-bit``):
            N/A

        id (List of ``int`` ``32-bit``):
            N/A

        random_id (List of ``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "shortcut_id", "id", "random_id"]

    ID = 0x6c750de1
    QUALNAME = "functions.messages.SendQuickReplyMessages"

    def __init__(self, *, peer: "raw.base.InputPeer", shortcut_id: int, id: List[int], random_id: List[int]) -> None:
        self.peer = peer
        self.shortcut_id = shortcut_id
        self.id = id
        self.random_id = random_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendQuickReplyMessages":
        
        peer = TLObject.read(b)
        
        shortcut_id = Int.read(b)
        
        id = TLObject.read(b, Int)
        
        random_id = TLObject.read(b, Long)
        
        return SendQuickReplyMessages(peer=peer, shortcut_id=shortcut_id, id=id, random_id=random_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.shortcut_id))
        
        b.write(Vector(self.id, Int))
        
        b.write(Vector(self.random_id, Long))
        
        return b.getvalue()

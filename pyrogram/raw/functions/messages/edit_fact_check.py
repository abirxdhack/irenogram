
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EditFactCheck(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``589EE75``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

        text (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "msg_id", "text"]

    ID = 0x589ee75
    QUALNAME = "functions.messages.EditFactCheck"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, text: "raw.base.TextWithEntities") -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.text = text

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditFactCheck":
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        text = TLObject.read(b)
        
        return EditFactCheck(peer=peer, msg_id=msg_id, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(self.text.write())
        
        return b.getvalue()

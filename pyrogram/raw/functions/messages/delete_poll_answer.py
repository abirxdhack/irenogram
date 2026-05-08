
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DeletePollAnswer(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``AC8505A5``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

        option (``bytes``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "msg_id", "option"]

    ID = 0xac8505a5
    QUALNAME = "functions.messages.DeletePollAnswer"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, option: bytes) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.option = option

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeletePollAnswer":
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        option = Bytes.read(b)
        
        return DeletePollAnswer(peer=peer, msg_id=msg_id, option=option)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Bytes(self.option))
        
        return b.getvalue()

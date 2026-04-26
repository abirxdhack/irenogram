
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AddPollAnswer(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``19BC4B6D``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

        answer (:obj:`PollAnswer <pyrogram.raw.base.PollAnswer>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "msg_id", "answer"]

    ID = 0x19bc4b6d
    QUALNAME = "functions.messages.AddPollAnswer"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, answer: "raw.base.PollAnswer") -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.answer = answer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AddPollAnswer":
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        answer = TLObject.read(b)
        
        return AddPollAnswer(peer=peer, msg_id=msg_id, answer=answer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(self.answer.write())
        
        return b.getvalue()

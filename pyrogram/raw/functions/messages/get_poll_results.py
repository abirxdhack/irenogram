
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetPollResults(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``EDA3E33B``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

        poll_hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "msg_id", "poll_hash"]

    ID = 0xeda3e33b
    QUALNAME = "functions.messages.GetPollResults"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, poll_hash: int) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.poll_hash = poll_hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPollResults":
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        poll_hash = Long.read(b)
        
        return GetPollResults(peer=peer, msg_id=msg_id, poll_hash=poll_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Long(self.poll_hash))
        
        return b.getvalue()

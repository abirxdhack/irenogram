
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateMessagePoll(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``D64C522B``

    Parameters:
        poll_id (``int`` ``64-bit``):
            N/A

        results (:obj:`PollResults <pyrogram.raw.base.PollResults>`):
            N/A

        peer (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        msg_id (``int`` ``32-bit``, *optional*):
            N/A

        top_msg_id (``int`` ``32-bit``, *optional*):
            N/A

        poll (:obj:`Poll <pyrogram.raw.base.Poll>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["poll_id", "results", "peer", "msg_id", "top_msg_id", "poll"]

    ID = 0xd64c522b
    QUALNAME = "types.UpdateMessagePoll"

    def __init__(self, *, poll_id: int, results: "raw.base.PollResults", peer: "raw.base.Peer" = None, msg_id: Optional[int] = None, top_msg_id: Optional[int] = None, poll: "raw.base.Poll" = None) -> None:
        self.poll_id = poll_id
        self.results = results
        self.peer = peer
        self.msg_id = msg_id
        self.top_msg_id = top_msg_id
        self.poll = poll

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateMessagePoll":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b) if flags & (1 << 1) else None
        
        msg_id = Int.read(b) if flags & (1 << 1) else None
        top_msg_id = Int.read(b) if flags & (1 << 2) else None
        poll_id = Long.read(b)
        
        poll = TLObject.read(b) if flags & (1 << 0) else None
        
        results = TLObject.read(b)
        
        return UpdateMessagePoll(poll_id=poll_id, results=results, peer=peer, msg_id=msg_id, top_msg_id=top_msg_id, poll=poll)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.peer is not None else 0
        flags |= (1 << 1) if self.msg_id is not None else 0
        flags |= (1 << 2) if self.top_msg_id is not None else 0
        flags |= (1 << 0) if self.poll is not None else 0
        b.write(Int(flags))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        if self.msg_id is not None:
            b.write(Int(self.msg_id))
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        b.write(Long(self.poll_id))
        
        if self.poll is not None:
            b.write(self.poll.write())
        
        b.write(self.results.write())
        
        return b.getvalue()

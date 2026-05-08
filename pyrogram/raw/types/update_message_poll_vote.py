
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateMessagePollVote(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``7699F014``

    Parameters:
        poll_id (``int`` ``64-bit``):
            N/A

        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        options (List of ``bytes``):
            N/A

        positions (List of ``int`` ``32-bit``):
            N/A

        qts (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["poll_id", "peer", "options", "positions", "qts"]

    ID = 0x7699f014
    QUALNAME = "types.UpdateMessagePollVote"

    def __init__(self, *, poll_id: int, peer: "raw.base.Peer", options: List[bytes], positions: List[int], qts: int) -> None:
        self.poll_id = poll_id
        self.peer = peer
        self.options = options
        self.positions = positions
        self.qts = qts

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateMessagePollVote":
        
        poll_id = Long.read(b)
        
        peer = TLObject.read(b)
        
        options = TLObject.read(b, Bytes)
        
        positions = TLObject.read(b, Int)
        
        qts = Int.read(b)
        
        return UpdateMessagePollVote(poll_id=poll_id, peer=peer, options=options, positions=positions, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.poll_id))
        
        b.write(self.peer.write())
        
        b.write(Vector(self.options, Bytes))
        
        b.write(Vector(self.positions, Int))
        
        b.write(Int(self.qts))
        
        return b.getvalue()

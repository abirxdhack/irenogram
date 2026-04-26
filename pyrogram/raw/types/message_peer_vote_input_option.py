
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessagePeerVoteInputOption(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessagePeerVote`.

    Details:
        - Layer: ``224``
        - ID: ``74CDA504``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        date (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["peer", "date"]

    ID = 0x74cda504
    QUALNAME = "types.MessagePeerVoteInputOption"

    def __init__(self, *, peer: "raw.base.Peer", date: int) -> None:
        self.peer = peer
        self.date = date

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessagePeerVoteInputOption":
        
        peer = TLObject.read(b)
        
        date = Int.read(b)
        
        return MessagePeerVoteInputOption(peer=peer, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.date))
        
        return b.getvalue()

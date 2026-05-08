
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessagePeerVote(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessagePeerVote`.

    Details:
        - Layer: ``224``
        - ID: ``B6CC2D5C``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        option (``bytes``):
            N/A

        date (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["peer", "option", "date"]

    ID = 0xb6cc2d5c
    QUALNAME = "types.MessagePeerVote"

    def __init__(self, *, peer: "raw.base.Peer", option: bytes, date: int) -> None:
        self.peer = peer
        self.option = option
        self.date = date

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessagePeerVote":
        
        peer = TLObject.read(b)
        
        option = Bytes.read(b)
        
        date = Int.read(b)
        
        return MessagePeerVote(peer=peer, option=option, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Bytes(self.option))
        
        b.write(Int(self.date))
        
        return b.getvalue()

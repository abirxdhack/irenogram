
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateBotChatBoost(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``904DD49C``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        boost (:obj:`Boost <pyrogram.raw.base.Boost>`):
            N/A

        qts (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["peer", "boost", "qts"]

    ID = 0x904dd49c
    QUALNAME = "types.UpdateBotChatBoost"

    def __init__(self, *, peer: "raw.base.Peer", boost: "raw.base.Boost", qts: int) -> None:
        self.peer = peer
        self.boost = boost
        self.qts = qts

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotChatBoost":
        
        peer = TLObject.read(b)
        
        boost = TLObject.read(b)
        
        qts = Int.read(b)
        
        return UpdateBotChatBoost(peer=peer, boost=boost, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(self.boost.write())
        
        b.write(Int(self.qts))
        
        return b.getvalue()

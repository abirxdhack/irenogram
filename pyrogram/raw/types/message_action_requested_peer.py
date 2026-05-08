
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageActionRequestedPeer(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``31518E9B``

    Parameters:
        button_id (``int`` ``32-bit``):
            N/A

        peers (List of :obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

    """

    __slots__: List[str] = ["button_id", "peers"]

    ID = 0x31518e9b
    QUALNAME = "types.MessageActionRequestedPeer"

    def __init__(self, *, button_id: int, peers: List["raw.base.Peer"]) -> None:
        self.button_id = button_id
        self.peers = peers

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionRequestedPeer":
        
        button_id = Int.read(b)
        
        peers = TLObject.read(b)
        
        return MessageActionRequestedPeer(button_id=button_id, peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.button_id))
        
        b.write(Vector(self.peers))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetPeerStories(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``2C4ADA50``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    Returns:
        :obj:`stories.PeerStories <pyrogram.raw.base.stories.PeerStories>`
    """

    __slots__: List[str] = ["peer"]

    ID = 0x2c4ada50
    QUALNAME = "functions.stories.GetPeerStories"

    def __init__(self, *, peer: "raw.base.InputPeer") -> None:
        self.peer = peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPeerStories":
        
        peer = TLObject.read(b)
        
        return GetPeerStories(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        return b.getvalue()

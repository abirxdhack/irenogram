
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReadStories(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A556DAC8``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        max_id (``int`` ``32-bit``):
            N/A

    Returns:
        List of ``int`` ``32-bit``
    """

    __slots__: List[str] = ["peer", "max_id"]

    ID = 0xa556dac8
    QUALNAME = "functions.stories.ReadStories"

    def __init__(self, *, peer: "raw.base.InputPeer", max_id: int) -> None:
        self.peer = peer
        self.max_id = max_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReadStories":
        
        peer = TLObject.read(b)
        
        max_id = Int.read(b)
        
        return ReadStories(peer=peer, max_id=max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.max_id))
        
        return b.getvalue()

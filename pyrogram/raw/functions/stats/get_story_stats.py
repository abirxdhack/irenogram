
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetStoryStats(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``374FEF40``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        id (``int`` ``32-bit``):
            N/A

        dark (``bool``, *optional*):
            N/A

    Returns:
        :obj:`stats.StoryStats <pyrogram.raw.base.stats.StoryStats>`
    """

    __slots__: List[str] = ["peer", "id", "dark"]

    ID = 0x374fef40
    QUALNAME = "functions.stats.GetStoryStats"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, dark: Optional[bool] = None) -> None:
        self.peer = peer
        self.id = id
        self.dark = dark

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStoryStats":
        
        flags = Int.read(b)
        
        dark = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        return GetStoryStats(peer=peer, id=id, dark=dark)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.dark else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        return b.getvalue()

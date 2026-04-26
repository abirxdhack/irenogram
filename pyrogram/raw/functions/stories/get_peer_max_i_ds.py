
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetPeerMaxIDs(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``78499170``

    Parameters:
        id (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    Returns:
        List of :obj:`RecentStory <pyrogram.raw.base.RecentStory>`
    """

    __slots__: List[str] = ["id"]

    ID = 0x78499170
    QUALNAME = "functions.stories.GetPeerMaxIDs"

    def __init__(self, *, id: List["raw.base.InputPeer"]) -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPeerMaxIDs":
        
        id = TLObject.read(b)
        
        return GetPeerMaxIDs(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.id))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetRecentReactions(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``39461DB2``

    Parameters:
        limit (``int`` ``32-bit``):
            N/A

        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`messages.Reactions <pyrogram.raw.base.messages.Reactions>`
    """

    __slots__: List[str] = ["limit", "hash"]

    ID = 0x39461db2
    QUALNAME = "functions.messages.GetRecentReactions"

    def __init__(self, *, limit: int, hash: int) -> None:
        self.limit = limit
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetRecentReactions":
        
        limit = Int.read(b)
        
        hash = Long.read(b)
        
        return GetRecentReactions(limit=limit, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.limit))
        
        b.write(Long(self.hash))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetOldFeaturedStickers(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``7ED094A1``

    Parameters:
        offset (``int`` ``32-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`messages.FeaturedStickers <pyrogram.raw.base.messages.FeaturedStickers>`
    """

    __slots__: List[str] = ["offset", "limit", "hash"]

    ID = 0x7ed094a1
    QUALNAME = "functions.messages.GetOldFeaturedStickers"

    def __init__(self, *, offset: int, limit: int, hash: int) -> None:
        self.offset = offset
        self.limit = limit
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetOldFeaturedStickers":
        
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        hash = Long.read(b)
        
        return GetOldFeaturedStickers(offset=offset, limit=limit, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        b.write(Long(self.hash))
        
        return b.getvalue()

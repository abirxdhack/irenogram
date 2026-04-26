
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetFeaturedStickers(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``64780B14``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`messages.FeaturedStickers <pyrogram.raw.base.messages.FeaturedStickers>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x64780b14
    QUALNAME = "functions.messages.GetFeaturedStickers"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFeaturedStickers":
        
        hash = Long.read(b)
        
        return GetFeaturedStickers(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        return b.getvalue()

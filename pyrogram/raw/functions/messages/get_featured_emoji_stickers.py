
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetFeaturedEmojiStickers(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``ECF6736``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`messages.FeaturedStickers <pyrogram.raw.base.messages.FeaturedStickers>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0xecf6736
    QUALNAME = "functions.messages.GetFeaturedEmojiStickers"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFeaturedEmojiStickers":
        
        hash = Long.read(b)
        
        return GetFeaturedEmojiStickers(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        return b.getvalue()

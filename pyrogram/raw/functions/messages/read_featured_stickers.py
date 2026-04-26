
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReadFeaturedStickers(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``5B118126``

    Parameters:
        id (List of ``int`` ``64-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id"]

    ID = 0x5b118126
    QUALNAME = "functions.messages.ReadFeaturedStickers"

    def __init__(self, *, id: List[int]) -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReadFeaturedStickers":
        
        id = TLObject.read(b, Long)
        
        return ReadFeaturedStickers(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.id, Long))
        
        return b.getvalue()

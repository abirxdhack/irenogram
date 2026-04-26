
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PhotoSizeProgressive(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PhotoSize`.

    Details:
        - Layer: ``224``
        - ID: ``FA3EFB95``

    Parameters:
        type (``str``):
            N/A

        w (``int`` ``32-bit``):
            N/A

        h (``int`` ``32-bit``):
            N/A

        sizes (List of ``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["type", "w", "h", "sizes"]

    ID = 0xfa3efb95
    QUALNAME = "types.PhotoSizeProgressive"

    def __init__(self, *, type: str, w: int, h: int, sizes: List[int]) -> None:
        self.type = type
        self.w = w
        self.h = h
        self.sizes = sizes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhotoSizeProgressive":
        
        type = String.read(b)
        
        w = Int.read(b)
        
        h = Int.read(b)
        
        sizes = TLObject.read(b, Int)
        
        return PhotoSizeProgressive(type=type, w=w, h=h, sizes=sizes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.type))
        
        b.write(Int(self.w))
        
        b.write(Int(self.h))
        
        b.write(Vector(self.sizes, Int))
        
        return b.getvalue()

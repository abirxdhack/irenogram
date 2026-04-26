
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MaskCoords(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MaskCoords`.

    Details:
        - Layer: ``224``
        - ID: ``AED6DBB2``

    Parameters:
        n (``int`` ``32-bit``):
            N/A

        x (``float`` ``64-bit``):
            N/A

        y (``float`` ``64-bit``):
            N/A

        zoom (``float`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["n", "x", "y", "zoom"]

    ID = 0xaed6dbb2
    QUALNAME = "types.MaskCoords"

    def __init__(self, *, n: int, x: float, y: float, zoom: float) -> None:
        self.n = n
        self.x = x
        self.y = y
        self.zoom = zoom

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MaskCoords":
        
        n = Int.read(b)
        
        x = Double.read(b)
        
        y = Double.read(b)
        
        zoom = Double.read(b)
        
        return MaskCoords(n=n, x=x, y=y, zoom=zoom)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.n))
        
        b.write(Double(self.x))
        
        b.write(Double(self.y))
        
        b.write(Double(self.zoom))
        
        return b.getvalue()

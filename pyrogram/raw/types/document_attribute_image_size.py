
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DocumentAttributeImageSize(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DocumentAttribute`.

    Details:
        - Layer: ``224``
        - ID: ``6C37C15C``

    Parameters:
        w (``int`` ``32-bit``):
            N/A

        h (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["w", "h"]

    ID = 0x6c37c15c
    QUALNAME = "types.DocumentAttributeImageSize"

    def __init__(self, *, w: int, h: int) -> None:
        self.w = w
        self.h = h

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeImageSize":
        
        w = Int.read(b)
        
        h = Int.read(b)
        
        return DocumentAttributeImageSize(w=w, h=h)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.w))
        
        b.write(Int(self.h))
        
        return b.getvalue()

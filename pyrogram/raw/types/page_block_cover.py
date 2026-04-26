
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PageBlockCover(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``39F23300``

    Parameters:
        cover (:obj:`PageBlock <pyrogram.raw.base.PageBlock>`):
            N/A

    """

    __slots__: List[str] = ["cover"]

    ID = 0x39f23300
    QUALNAME = "types.PageBlockCover"

    def __init__(self, *, cover: "raw.base.PageBlock") -> None:
        self.cover = cover

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockCover":
        
        cover = TLObject.read(b)
        
        return PageBlockCover(cover=cover)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.cover.write())
        
        return b.getvalue()

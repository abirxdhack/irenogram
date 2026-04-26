
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PageBlockCollage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``65A0FA4D``

    Parameters:
        items (List of :obj:`PageBlock <pyrogram.raw.base.PageBlock>`):
            N/A

        caption (:obj:`PageCaption <pyrogram.raw.base.PageCaption>`):
            N/A

    """

    __slots__: List[str] = ["items", "caption"]

    ID = 0x65a0fa4d
    QUALNAME = "types.PageBlockCollage"

    def __init__(self, *, items: List["raw.base.PageBlock"], caption: "raw.base.PageCaption") -> None:
        self.items = items
        self.caption = caption

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockCollage":
        
        items = TLObject.read(b)
        
        caption = TLObject.read(b)
        
        return PageBlockCollage(items=items, caption=caption)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.items))
        
        b.write(self.caption.write())
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PageBlockBlockquote(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``263D7C26``

    Parameters:
        text (:obj:`RichText <pyrogram.raw.base.RichText>`):
            N/A

        caption (:obj:`RichText <pyrogram.raw.base.RichText>`):
            N/A

    """

    __slots__: List[str] = ["text", "caption"]

    ID = 0x263d7c26
    QUALNAME = "types.PageBlockBlockquote"

    def __init__(self, *, text: "raw.base.RichText", caption: "raw.base.RichText") -> None:
        self.text = text
        self.caption = caption

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockBlockquote":
        
        text = TLObject.read(b)
        
        caption = TLObject.read(b)
        
        return PageBlockBlockquote(text=text, caption=caption)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.text.write())
        
        b.write(self.caption.write())
        
        return b.getvalue()

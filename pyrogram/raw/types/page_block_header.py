
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PageBlockHeader(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``BFD064EC``

    Parameters:
        text (:obj:`RichText <pyrogram.raw.base.RichText>`):
            N/A

    """

    __slots__: List[str] = ["text"]

    ID = 0xbfd064ec
    QUALNAME = "types.PageBlockHeader"

    def __init__(self, *, text: "raw.base.RichText") -> None:
        self.text = text

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockHeader":
        
        text = TLObject.read(b)
        
        return PageBlockHeader(text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.text.write())
        
        return b.getvalue()

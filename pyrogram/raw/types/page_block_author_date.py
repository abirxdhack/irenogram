
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PageBlockAuthorDate(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``BAAFE5E0``

    Parameters:
        author (:obj:`RichText <pyrogram.raw.base.RichText>`):
            N/A

        published_date (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["author", "published_date"]

    ID = 0xbaafe5e0
    QUALNAME = "types.PageBlockAuthorDate"

    def __init__(self, *, author: "raw.base.RichText", published_date: int) -> None:
        self.author = author
        self.published_date = published_date

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockAuthorDate":
        
        author = TLObject.read(b)
        
        published_date = Int.read(b)
        
        return PageBlockAuthorDate(author=author, published_date=published_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.author.write())
        
        b.write(Int(self.published_date))
        
        return b.getvalue()

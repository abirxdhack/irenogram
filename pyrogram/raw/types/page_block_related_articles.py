
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PageBlockRelatedArticles(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``16115A96``

    Parameters:
        title (:obj:`RichText <pyrogram.raw.base.RichText>`):
            N/A

        articles (List of :obj:`PageRelatedArticle <pyrogram.raw.base.PageRelatedArticle>`):
            N/A

    """

    __slots__: List[str] = ["title", "articles"]

    ID = 0x16115a96
    QUALNAME = "types.PageBlockRelatedArticles"

    def __init__(self, *, title: "raw.base.RichText", articles: List["raw.base.PageRelatedArticle"]) -> None:
        self.title = title
        self.articles = articles

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockRelatedArticles":
        
        title = TLObject.read(b)
        
        articles = TLObject.read(b)
        
        return PageBlockRelatedArticles(title=title, articles=articles)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.title.write())
        
        b.write(Vector(self.articles))
        
        return b.getvalue()

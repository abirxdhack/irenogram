
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EmojiKeywordDeleted(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.EmojiKeyword`.

    Details:
        - Layer: ``224``
        - ID: ``236DF622``

    Parameters:
        keyword (``str``):
            N/A

        emoticons (List of ``str``):
            N/A

    """

    __slots__: List[str] = ["keyword", "emoticons"]

    ID = 0x236df622
    QUALNAME = "types.EmojiKeywordDeleted"

    def __init__(self, *, keyword: str, emoticons: List[str]) -> None:
        self.keyword = keyword
        self.emoticons = emoticons

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiKeywordDeleted":
        
        keyword = String.read(b)
        
        emoticons = TLObject.read(b, String)
        
        return EmojiKeywordDeleted(keyword=keyword, emoticons=emoticons)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.keyword))
        
        b.write(Vector(self.emoticons, String))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EmojiKeyword(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.EmojiKeyword`.

    Details:
        - Layer: ``224``
        - ID: ``D5B3B9F9``

    Parameters:
        keyword (``str``):
            N/A

        emoticons (List of ``str``):
            N/A

    """

    __slots__: List[str] = ["keyword", "emoticons"]

    ID = 0xd5b3b9f9
    QUALNAME = "types.EmojiKeyword"

    def __init__(self, *, keyword: str, emoticons: List[str]) -> None:
        self.keyword = keyword
        self.emoticons = emoticons

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiKeyword":
        
        keyword = String.read(b)
        
        emoticons = TLObject.read(b, String)
        
        return EmojiKeyword(keyword=keyword, emoticons=emoticons)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.keyword))
        
        b.write(Vector(self.emoticons, String))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SearchCustomEmoji(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``2C11C0D7``

    Parameters:
        emoticon (``str``):
            N/A

        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`EmojiList <pyrogram.raw.base.EmojiList>`
    """

    __slots__: List[str] = ["emoticon", "hash"]

    ID = 0x2c11c0d7
    QUALNAME = "functions.messages.SearchCustomEmoji"

    def __init__(self, *, emoticon: str, hash: int) -> None:
        self.emoticon = emoticon
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchCustomEmoji":
        
        emoticon = String.read(b)
        
        hash = Long.read(b)
        
        return SearchCustomEmoji(emoticon=emoticon, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.emoticon))
        
        b.write(Long(self.hash))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SearchStickers(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``29B1C66A``

    Parameters:
        q (``str``):
            N/A

        emoticon (``str``):
            N/A

        lang_code (List of ``str``):
            N/A

        offset (``int`` ``32-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        hash (``int`` ``64-bit``):
            N/A

        emojis (``bool``, *optional*):
            N/A

    Returns:
        :obj:`messages.FoundStickers <pyrogram.raw.base.messages.FoundStickers>`
    """

    __slots__: List[str] = ["q", "emoticon", "lang_code", "offset", "limit", "hash", "emojis"]

    ID = 0x29b1c66a
    QUALNAME = "functions.messages.SearchStickers"

    def __init__(self, *, q: str, emoticon: str, lang_code: List[str], offset: int, limit: int, hash: int, emojis: Optional[bool] = None) -> None:
        self.q = q
        self.emoticon = emoticon
        self.lang_code = lang_code
        self.offset = offset
        self.limit = limit
        self.hash = hash
        self.emojis = emojis

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchStickers":
        
        flags = Int.read(b)
        
        emojis = True if flags & (1 << 0) else False
        q = String.read(b)
        
        emoticon = String.read(b)
        
        lang_code = TLObject.read(b, String)
        
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        hash = Long.read(b)
        
        return SearchStickers(q=q, emoticon=emoticon, lang_code=lang_code, offset=offset, limit=limit, hash=hash, emojis=emojis)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.emojis else 0
        b.write(Int(flags))
        
        b.write(String(self.q))
        
        b.write(String(self.emoticon))
        
        b.write(Vector(self.lang_code, String))
        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        b.write(Long(self.hash))
        
        return b.getvalue()

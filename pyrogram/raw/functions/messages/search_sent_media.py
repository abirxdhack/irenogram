
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SearchSentMedia(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``107E31A0``

    Parameters:
        q (``str``):
            N/A

        filter (:obj:`MessagesFilter <pyrogram.raw.base.MessagesFilter>`):
            N/A

        limit (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.Messages <pyrogram.raw.base.messages.Messages>`
    """

    __slots__: List[str] = ["q", "filter", "limit"]

    ID = 0x107e31a0
    QUALNAME = "functions.messages.SearchSentMedia"

    def __init__(self, *, q: str, filter: "raw.base.MessagesFilter", limit: int) -> None:
        self.q = q
        self.filter = filter
        self.limit = limit

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchSentMedia":
        
        q = String.read(b)
        
        filter = TLObject.read(b)
        
        limit = Int.read(b)
        
        return SearchSentMedia(q=q, filter=filter, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.q))
        
        b.write(self.filter.write())
        
        b.write(Int(self.limit))
        
        return b.getvalue()

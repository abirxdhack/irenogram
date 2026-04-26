
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class Search(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``11F812D8``

    Parameters:
        q (``str``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`contacts.Found <pyrogram.raw.base.contacts.Found>`
    """

    __slots__: List[str] = ["q", "limit"]

    ID = 0x11f812d8
    QUALNAME = "functions.contacts.Search"

    def __init__(self, *, q: str, limit: int) -> None:
        self.q = q
        self.limit = limit

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Search":
        
        q = String.read(b)
        
        limit = Int.read(b)
        
        return Search(q=q, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.q))
        
        b.write(Int(self.limit))
        
        return b.getvalue()

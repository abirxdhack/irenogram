
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SearchPostsFlood(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SearchPostsFlood`.

    Details:
        - Layer: ``224``
        - ID: ``3E0B5B6A``

    Parameters:
        total_daily (``int`` ``32-bit``):
            N/A

        remains (``int`` ``32-bit``):
            N/A

        stars_amount (``int`` ``64-bit``):
            N/A

        query_is_free (``bool``, *optional*):
            N/A

        wait_till (``int`` ``32-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            channels.CheckSearchPostsFlood
    """

    __slots__: List[str] = ["total_daily", "remains", "stars_amount", "query_is_free", "wait_till"]

    ID = 0x3e0b5b6a
    QUALNAME = "types.SearchPostsFlood"

    def __init__(self, *, total_daily: int, remains: int, stars_amount: int, query_is_free: Optional[bool] = None, wait_till: Optional[int] = None) -> None:
        self.total_daily = total_daily
        self.remains = remains
        self.stars_amount = stars_amount
        self.query_is_free = query_is_free
        self.wait_till = wait_till

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchPostsFlood":
        
        flags = Int.read(b)
        
        query_is_free = True if flags & (1 << 0) else False
        total_daily = Int.read(b)
        
        remains = Int.read(b)
        
        wait_till = Int.read(b) if flags & (1 << 1) else None
        stars_amount = Long.read(b)
        
        return SearchPostsFlood(total_daily=total_daily, remains=remains, stars_amount=stars_amount, query_is_free=query_is_free, wait_till=wait_till)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.query_is_free else 0
        flags |= (1 << 1) if self.wait_till is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.total_daily))
        
        b.write(Int(self.remains))
        
        if self.wait_till is not None:
            b.write(Int(self.wait_till))
        
        b.write(Long(self.stars_amount))
        
        return b.getvalue()

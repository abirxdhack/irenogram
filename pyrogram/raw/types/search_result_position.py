
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SearchResultPosition(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SearchResultsPosition`.

    Details:
        - Layer: ``224``
        - ID: ``7F648B67``

    Parameters:
        msg_id (``int`` ``32-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        offset (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["msg_id", "date", "offset"]

    ID = 0x7f648b67
    QUALNAME = "types.SearchResultPosition"

    def __init__(self, *, msg_id: int, date: int, offset: int) -> None:
        self.msg_id = msg_id
        self.date = date
        self.offset = offset

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchResultPosition":
        
        msg_id = Int.read(b)
        
        date = Int.read(b)
        
        offset = Int.read(b)
        
        return SearchResultPosition(msg_id=msg_id, date=date, offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.msg_id))
        
        b.write(Int(self.date))
        
        b.write(Int(self.offset))
        
        return b.getvalue()

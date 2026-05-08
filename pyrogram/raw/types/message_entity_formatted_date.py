
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageEntityFormattedDate(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageEntity`.

    Details:
        - Layer: ``224``
        - ID: ``904AC7C7``

    Parameters:
        offset (``int`` ``32-bit``):
            N/A

        length (``int`` ``32-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        relative (``bool``, *optional*):
            N/A

        short_time (``bool``, *optional*):
            N/A

        long_time (``bool``, *optional*):
            N/A

        short_date (``bool``, *optional*):
            N/A

        long_date (``bool``, *optional*):
            N/A

        day_of_week (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["offset", "length", "date", "relative", "short_time", "long_time", "short_date", "long_date", "day_of_week"]

    ID = 0x904ac7c7
    QUALNAME = "types.MessageEntityFormattedDate"

    def __init__(self, *, offset: int, length: int, date: int, relative: Optional[bool] = None, short_time: Optional[bool] = None, long_time: Optional[bool] = None, short_date: Optional[bool] = None, long_date: Optional[bool] = None, day_of_week: Optional[bool] = None) -> None:
        self.offset = offset
        self.length = length
        self.date = date
        self.relative = relative
        self.short_time = short_time
        self.long_time = long_time
        self.short_date = short_date
        self.long_date = long_date
        self.day_of_week = day_of_week

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEntityFormattedDate":
        
        flags = Int.read(b)
        
        relative = True if flags & (1 << 0) else False
        short_time = True if flags & (1 << 1) else False
        long_time = True if flags & (1 << 2) else False
        short_date = True if flags & (1 << 3) else False
        long_date = True if flags & (1 << 4) else False
        day_of_week = True if flags & (1 << 5) else False
        offset = Int.read(b)
        
        length = Int.read(b)
        
        date = Int.read(b)
        
        return MessageEntityFormattedDate(offset=offset, length=length, date=date, relative=relative, short_time=short_time, long_time=long_time, short_date=short_date, long_date=long_date, day_of_week=day_of_week)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.relative else 0
        flags |= (1 << 1) if self.short_time else 0
        flags |= (1 << 2) if self.long_time else 0
        flags |= (1 << 3) if self.short_date else 0
        flags |= (1 << 4) if self.long_date else 0
        flags |= (1 << 5) if self.day_of_week else 0
        b.write(Int(flags))
        
        b.write(Int(self.offset))
        
        b.write(Int(self.length))
        
        b.write(Int(self.date))
        
        return b.getvalue()

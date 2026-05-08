
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DraftMessageEmpty(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DraftMessage`.

    Details:
        - Layer: ``224``
        - ID: ``1B0C841A``

    Parameters:
        date (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["date"]

    ID = 0x1b0c841a
    QUALNAME = "types.DraftMessageEmpty"

    def __init__(self, *, date: Optional[int] = None) -> None:
        self.date = date

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DraftMessageEmpty":
        
        flags = Int.read(b)
        
        date = Int.read(b) if flags & (1 << 0) else None
        return DraftMessageEmpty(date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.date is not None else 0
        b.write(Int(flags))
        
        if self.date is not None:
            b.write(Int(self.date))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StatsAbsValueAndPrev(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StatsAbsValueAndPrev`.

    Details:
        - Layer: ``224``
        - ID: ``CB43ACDE``

    Parameters:
        current (``float`` ``64-bit``):
            N/A

        previous (``float`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["current", "previous"]

    ID = 0xcb43acde
    QUALNAME = "types.StatsAbsValueAndPrev"

    def __init__(self, *, current: float, previous: float) -> None:
        self.current = current
        self.previous = previous

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StatsAbsValueAndPrev":
        
        current = Double.read(b)
        
        previous = Double.read(b)
        
        return StatsAbsValueAndPrev(current=current, previous=previous)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Double(self.current))
        
        b.write(Double(self.previous))
        
        return b.getvalue()

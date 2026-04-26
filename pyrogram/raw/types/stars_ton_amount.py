
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StarsTonAmount(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarsAmount`.

    Details:
        - Layer: ``224``
        - ID: ``74AEE3E0``

    Parameters:
        amount (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["amount"]

    ID = 0x74aee3e0
    QUALNAME = "types.StarsTonAmount"

    def __init__(self, *, amount: int) -> None:
        self.amount = amount

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsTonAmount":
        
        amount = Long.read(b)
        
        return StarsTonAmount(amount=amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.amount))
        
        return b.getvalue()

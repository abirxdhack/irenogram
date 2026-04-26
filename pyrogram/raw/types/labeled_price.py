
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class LabeledPrice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.LabeledPrice`.

    Details:
        - Layer: ``224``
        - ID: ``CB296BF8``

    Parameters:
        label (``str``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["label", "amount"]

    ID = 0xcb296bf8
    QUALNAME = "types.LabeledPrice"

    def __init__(self, *, label: str, amount: int) -> None:
        self.label = label
        self.amount = amount

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LabeledPrice":
        
        label = String.read(b)
        
        amount = Long.read(b)
        
        return LabeledPrice(label=label, amount=amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.label))
        
        b.write(Long(self.amount))
        
        return b.getvalue()

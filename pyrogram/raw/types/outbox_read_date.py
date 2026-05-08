
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class OutboxReadDate(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.OutboxReadDate`.

    Details:
        - Layer: ``224``
        - ID: ``3BB842AC``

    Parameters:
        date (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetOutboxReadDate
    """

    __slots__: List[str] = ["date"]

    ID = 0x3bb842ac
    QUALNAME = "types.OutboxReadDate"

    def __init__(self, *, date: int) -> None:
        self.date = date

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "OutboxReadDate":
        
        date = Int.read(b)
        
        return OutboxReadDate(date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.date))
        
        return b.getvalue()

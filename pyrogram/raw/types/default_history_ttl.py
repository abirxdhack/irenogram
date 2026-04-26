
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DefaultHistoryTTL(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DefaultHistoryTTL`.

    Details:
        - Layer: ``224``
        - ID: ``43B46B20``

    Parameters:
        period (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetDefaultHistoryTTL
    """

    __slots__: List[str] = ["period"]

    ID = 0x43b46b20
    QUALNAME = "types.DefaultHistoryTTL"

    def __init__(self, *, period: int) -> None:
        self.period = period

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DefaultHistoryTTL":
        
        period = Int.read(b)
        
        return DefaultHistoryTTL(period=period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.period))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateDeviceLocked(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``38DF3532``

    Parameters:
        period (``int`` ``32-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["period"]

    ID = 0x38df3532
    QUALNAME = "functions.account.UpdateDeviceLocked"

    def __init__(self, *, period: int) -> None:
        self.period = period

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDeviceLocked":
        
        period = Int.read(b)
        
        return UpdateDeviceLocked(period=period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.period))
        
        return b.getvalue()

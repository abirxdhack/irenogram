
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetAvailableEffects(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``DEA20A39``

    Parameters:
        hash (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.AvailableEffects <pyrogram.raw.base.messages.AvailableEffects>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0xdea20a39
    QUALNAME = "functions.messages.GetAvailableEffects"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAvailableEffects":
        
        hash = Int.read(b)
        
        return GetAvailableEffects(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.hash))
        
        return b.getvalue()

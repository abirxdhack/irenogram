
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetAvailableReactions(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``18DEA0AC``

    Parameters:
        hash (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.AvailableReactions <pyrogram.raw.base.messages.AvailableReactions>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x18dea0ac
    QUALNAME = "functions.messages.GetAvailableReactions"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAvailableReactions":
        
        hash = Int.read(b)
        
        return GetAvailableReactions(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.hash))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetAllStickers(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``B8A0A1A8``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`messages.AllStickers <pyrogram.raw.base.messages.AllStickers>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0xb8a0a1a8
    QUALNAME = "functions.messages.GetAllStickers"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAllStickers":
        
        hash = Long.read(b)
        
        return GetAllStickers(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        return b.getvalue()

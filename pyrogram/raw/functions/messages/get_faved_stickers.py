
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetFavedStickers(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``4F1AAA9``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`messages.FavedStickers <pyrogram.raw.base.messages.FavedStickers>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x4f1aaa9
    QUALNAME = "functions.messages.GetFavedStickers"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFavedStickers":
        
        hash = Long.read(b)
        
        return GetFavedStickers(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetSavedGifs(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``5CF09635``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`messages.SavedGifs <pyrogram.raw.base.messages.SavedGifs>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x5cf09635
    QUALNAME = "functions.messages.GetSavedGifs"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSavedGifs":
        
        hash = Long.read(b)
        
        return GetSavedGifs(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        return b.getvalue()

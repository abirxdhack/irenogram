
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetMyStickers(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D0B5E1FC``

    Parameters:
        offset_id (``int`` ``64-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.MyStickers <pyrogram.raw.base.messages.MyStickers>`
    """

    __slots__: List[str] = ["offset_id", "limit"]

    ID = 0xd0b5e1fc
    QUALNAME = "functions.messages.GetMyStickers"

    def __init__(self, *, offset_id: int, limit: int) -> None:
        self.offset_id = offset_id
        self.limit = limit

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMyStickers":
        
        offset_id = Long.read(b)
        
        limit = Int.read(b)
        
        return GetMyStickers(offset_id=offset_id, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.offset_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()

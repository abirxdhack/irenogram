
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StarGiftAttributeIdBackdrop(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAttributeId`.

    Details:
        - Layer: ``224``
        - ID: ``1F01C757``

    Parameters:
        backdrop_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["backdrop_id"]

    ID = 0x1f01c757
    QUALNAME = "types.StarGiftAttributeIdBackdrop"

    def __init__(self, *, backdrop_id: int) -> None:
        self.backdrop_id = backdrop_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAttributeIdBackdrop":
        
        backdrop_id = Int.read(b)
        
        return StarGiftAttributeIdBackdrop(backdrop_id=backdrop_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.backdrop_id))
        
        return b.getvalue()

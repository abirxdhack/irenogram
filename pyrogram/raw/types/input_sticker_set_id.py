
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputStickerSetID(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputStickerSet`.

    Details:
        - Layer: ``224``
        - ID: ``9DE7A269``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        access_hash (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["id", "access_hash"]

    ID = 0x9de7a269
    QUALNAME = "types.InputStickerSetID"

    def __init__(self, *, id: int, access_hash: int) -> None:
        self.id = id
        self.access_hash = access_hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStickerSetID":
        
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        return InputStickerSetID(id=id, access_hash=access_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        return b.getvalue()

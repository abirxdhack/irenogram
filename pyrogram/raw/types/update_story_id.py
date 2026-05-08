
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateStoryID(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``1BF335B9``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        random_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["id", "random_id"]

    ID = 0x1bf335b9
    QUALNAME = "types.UpdateStoryID"

    def __init__(self, *, id: int, random_id: int) -> None:
        self.id = id
        self.random_id = random_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStoryID":
        
        id = Int.read(b)
        
        random_id = Long.read(b)
        
        return UpdateStoryID(id=id, random_id=random_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.id))
        
        b.write(Long(self.random_id))
        
        return b.getvalue()

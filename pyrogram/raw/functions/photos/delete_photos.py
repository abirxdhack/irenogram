
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DeletePhotos(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``87CF7F2F``

    Parameters:
        id (List of :obj:`InputPhoto <pyrogram.raw.base.InputPhoto>`):
            N/A

    Returns:
        List of ``int`` ``64-bit``
    """

    __slots__: List[str] = ["id"]

    ID = 0x87cf7f2f
    QUALNAME = "functions.photos.DeletePhotos"

    def __init__(self, *, id: List["raw.base.InputPhoto"]) -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeletePhotos":
        
        id = TLObject.read(b)
        
        return DeletePhotos(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.id))
        
        return b.getvalue()

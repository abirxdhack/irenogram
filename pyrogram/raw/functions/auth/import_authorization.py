
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ImportAuthorization(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A57A7DAD``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        bytes (``bytes``):
            N/A

    Returns:
        :obj:`auth.Authorization <pyrogram.raw.base.auth.Authorization>`
    """

    __slots__: List[str] = ["id", "bytes"]

    ID = 0xa57a7dad
    QUALNAME = "functions.auth.ImportAuthorization"

    def __init__(self, *, id: int, bytes: bytes) -> None:
        self.id = id
        self.bytes = bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ImportAuthorization":
        
        id = Long.read(b)
        
        bytes = Bytes.read(b)
        
        return ImportAuthorization(id=id, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        
        b.write(Bytes(self.bytes))
        
        return b.getvalue()

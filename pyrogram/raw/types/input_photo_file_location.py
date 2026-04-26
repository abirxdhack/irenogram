
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputPhotoFileLocation(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputFileLocation`.

    Details:
        - Layer: ``224``
        - ID: ``40181FFE``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        access_hash (``int`` ``64-bit``):
            N/A

        file_reference (``bytes``):
            N/A

        thumb_size (``str``):
            N/A

    """

    __slots__: List[str] = ["id", "access_hash", "file_reference", "thumb_size"]

    ID = 0x40181ffe
    QUALNAME = "types.InputPhotoFileLocation"

    def __init__(self, *, id: int, access_hash: int, file_reference: bytes, thumb_size: str) -> None:
        self.id = id
        self.access_hash = access_hash
        self.file_reference = file_reference
        self.thumb_size = thumb_size

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPhotoFileLocation":
        
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        file_reference = Bytes.read(b)
        
        thumb_size = String.read(b)
        
        return InputPhotoFileLocation(id=id, access_hash=access_hash, file_reference=file_reference, thumb_size=thumb_size)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Bytes(self.file_reference))
        
        b.write(String(self.thumb_size))
        
        return b.getvalue()

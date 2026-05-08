
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SaveFilePart(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``B304A621``

    Parameters:
        file_id (``int`` ``64-bit``):
            N/A

        file_part (``int`` ``32-bit``):
            N/A

        bytes (``bytes``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["file_id", "file_part", "bytes"]

    ID = 0xb304a621
    QUALNAME = "functions.upload.SaveFilePart"

    def __init__(self, *, file_id: int, file_part: int, bytes: bytes) -> None:
        self.file_id = file_id
        self.file_part = file_part
        self.bytes = bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveFilePart":
        
        file_id = Long.read(b)
        
        file_part = Int.read(b)
        
        bytes = Bytes.read(b)
        
        return SaveFilePart(file_id=file_id, file_part=file_part, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.file_id))
        
        b.write(Int(self.file_part))
        
        b.write(Bytes(self.bytes))
        
        return b.getvalue()

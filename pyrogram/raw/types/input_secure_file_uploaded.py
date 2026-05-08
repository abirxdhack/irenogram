
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputSecureFileUploaded(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputSecureFile`.

    Details:
        - Layer: ``224``
        - ID: ``3334B0F0``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        parts (``int`` ``32-bit``):
            N/A

        md5_checksum (``str``):
            N/A

        file_hash (``bytes``):
            N/A

        secret (``bytes``):
            N/A

    """

    __slots__: List[str] = ["id", "parts", "md5_checksum", "file_hash", "secret"]

    ID = 0x3334b0f0
    QUALNAME = "types.InputSecureFileUploaded"

    def __init__(self, *, id: int, parts: int, md5_checksum: str, file_hash: bytes, secret: bytes) -> None:
        self.id = id
        self.parts = parts
        self.md5_checksum = md5_checksum
        self.file_hash = file_hash
        self.secret = secret

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputSecureFileUploaded":
        
        id = Long.read(b)
        
        parts = Int.read(b)
        
        md5_checksum = String.read(b)
        
        file_hash = Bytes.read(b)
        
        secret = Bytes.read(b)
        
        return InputSecureFileUploaded(id=id, parts=parts, md5_checksum=md5_checksum, file_hash=file_hash, secret=secret)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        
        b.write(Int(self.parts))
        
        b.write(String(self.md5_checksum))
        
        b.write(Bytes(self.file_hash))
        
        b.write(Bytes(self.secret))
        
        return b.getvalue()

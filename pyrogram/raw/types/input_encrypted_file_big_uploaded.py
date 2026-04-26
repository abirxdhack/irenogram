
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputEncryptedFileBigUploaded(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputEncryptedFile`.

    Details:
        - Layer: ``224``
        - ID: ``2DC173C8``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        parts (``int`` ``32-bit``):
            N/A

        key_fingerprint (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["id", "parts", "key_fingerprint"]

    ID = 0x2dc173c8
    QUALNAME = "types.InputEncryptedFileBigUploaded"

    def __init__(self, *, id: int, parts: int, key_fingerprint: int) -> None:
        self.id = id
        self.parts = parts
        self.key_fingerprint = key_fingerprint

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputEncryptedFileBigUploaded":
        
        id = Long.read(b)
        
        parts = Int.read(b)
        
        key_fingerprint = Int.read(b)
        
        return InputEncryptedFileBigUploaded(id=id, parts=parts, key_fingerprint=key_fingerprint)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        
        b.write(Int(self.parts))
        
        b.write(Int(self.key_fingerprint))
        
        return b.getvalue()

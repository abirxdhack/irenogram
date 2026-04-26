
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EncryptedFile(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.EncryptedFile`.

    Details:
        - Layer: ``224``
        - ID: ``A8008CD8``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        access_hash (``int`` ``64-bit``):
            N/A

        size (``int`` ``64-bit``):
            N/A

        dc_id (``int`` ``32-bit``):
            N/A

        key_fingerprint (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadEncryptedFile
    """

    __slots__: List[str] = ["id", "access_hash", "size", "dc_id", "key_fingerprint"]

    ID = 0xa8008cd8
    QUALNAME = "types.EncryptedFile"

    def __init__(self, *, id: int, access_hash: int, size: int, dc_id: int, key_fingerprint: int) -> None:
        self.id = id
        self.access_hash = access_hash
        self.size = size
        self.dc_id = dc_id
        self.key_fingerprint = key_fingerprint

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EncryptedFile":
        
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        size = Long.read(b)
        
        dc_id = Int.read(b)
        
        key_fingerprint = Int.read(b)
        
        return EncryptedFile(id=id, access_hash=access_hash, size=size, dc_id=dc_id, key_fingerprint=key_fingerprint)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Long(self.size))
        
        b.write(Int(self.dc_id))
        
        b.write(Int(self.key_fingerprint))
        
        return b.getvalue()

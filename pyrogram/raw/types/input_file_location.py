
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputFileLocation(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputFileLocation`.

    Details:
        - Layer: ``224``
        - ID: ``DFDAABE1``

    Parameters:
        volume_id (``int`` ``64-bit``):
            N/A

        local_id (``int`` ``32-bit``):
            N/A

        secret (``int`` ``64-bit``):
            N/A

        file_reference (``bytes``):
            N/A

    """

    __slots__: List[str] = ["volume_id", "local_id", "secret", "file_reference"]

    ID = 0xdfdaabe1
    QUALNAME = "types.InputFileLocation"

    def __init__(self, *, volume_id: int, local_id: int, secret: int, file_reference: bytes) -> None:
        self.volume_id = volume_id
        self.local_id = local_id
        self.secret = secret
        self.file_reference = file_reference

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputFileLocation":
        
        volume_id = Long.read(b)
        
        local_id = Int.read(b)
        
        secret = Long.read(b)
        
        file_reference = Bytes.read(b)
        
        return InputFileLocation(volume_id=volume_id, local_id=local_id, secret=secret, file_reference=file_reference)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.volume_id))
        
        b.write(Int(self.local_id))
        
        b.write(Long(self.secret))
        
        b.write(Bytes(self.file_reference))
        
        return b.getvalue()

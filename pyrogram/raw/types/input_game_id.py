
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputGameID(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputGame`.

    Details:
        - Layer: ``224``
        - ID: ``32C3E77``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        access_hash (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["id", "access_hash"]

    ID = 0x32c3e77
    QUALNAME = "types.InputGameID"

    def __init__(self, *, id: int, access_hash: int) -> None:
        self.id = id
        self.access_hash = access_hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputGameID":
        
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        return InputGameID(id=id, access_hash=access_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        return b.getvalue()

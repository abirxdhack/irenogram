
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputBotAppID(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputBotApp`.

    Details:
        - Layer: ``224``
        - ID: ``A920BD7A``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        access_hash (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["id", "access_hash"]

    ID = 0xa920bd7a
    QUALNAME = "types.InputBotAppID"

    def __init__(self, *, id: int, access_hash: int) -> None:
        self.id = id
        self.access_hash = access_hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotAppID":
        
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        return InputBotAppID(id=id, access_hash=access_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        return b.getvalue()

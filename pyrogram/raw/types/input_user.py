
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputUser(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputUser`.

    Details:
        - Layer: ``224``
        - ID: ``F21158C6``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        access_hash (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["user_id", "access_hash"]

    ID = 0xf21158c6
    QUALNAME = "types.InputUser"

    def __init__(self, *, user_id: int, access_hash: int) -> None:
        self.user_id = user_id
        self.access_hash = access_hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputUser":
        
        user_id = Long.read(b)
        
        access_hash = Long.read(b)
        
        return InputUser(user_id=user_id, access_hash=access_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.user_id))
        
        b.write(Long(self.access_hash))
        
        return b.getvalue()

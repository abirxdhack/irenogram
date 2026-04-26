
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateUserPhone(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``5492A13``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        phone (``str``):
            N/A

    """

    __slots__: List[str] = ["user_id", "phone"]

    ID = 0x5492a13
    QUALNAME = "types.UpdateUserPhone"

    def __init__(self, *, user_id: int, phone: str) -> None:
        self.user_id = user_id
        self.phone = phone

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateUserPhone":
        
        user_id = Long.read(b)
        
        phone = String.read(b)
        
        return UpdateUserPhone(user_id=user_id, phone=phone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.user_id))
        
        b.write(String(self.phone))
        
        return b.getvalue()

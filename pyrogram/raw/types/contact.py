
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class Contact(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Contact`.

    Details:
        - Layer: ``224``
        - ID: ``145ADE0B``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        mutual (``bool``):
            N/A

    """

    __slots__: List[str] = ["user_id", "mutual"]

    ID = 0x145ade0b
    QUALNAME = "types.Contact"

    def __init__(self, *, user_id: int, mutual: bool) -> None:
        self.user_id = user_id
        self.mutual = mutual

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Contact":
        
        user_id = Long.read(b)
        
        mutual = Bool.read(b)
        
        return Contact(user_id=user_id, mutual=mutual)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.user_id))
        
        b.write(Bool(self.mutual))
        
        return b.getvalue()

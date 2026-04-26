
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EditCloseFriends(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``BA6705F0``

    Parameters:
        id (List of ``int`` ``64-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id"]

    ID = 0xba6705f0
    QUALNAME = "functions.contacts.EditCloseFriends"

    def __init__(self, *, id: List[int]) -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditCloseFriends":
        
        id = TLObject.read(b, Long)
        
        return EditCloseFriends(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.id, Long))
        
        return b.getvalue()

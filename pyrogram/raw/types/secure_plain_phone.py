
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SecurePlainPhone(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SecurePlainData`.

    Details:
        - Layer: ``224``
        - ID: ``7D6099DD``

    Parameters:
        phone (``str``):
            N/A

    """

    __slots__: List[str] = ["phone"]

    ID = 0x7d6099dd
    QUALNAME = "types.SecurePlainPhone"

    def __init__(self, *, phone: str) -> None:
        self.phone = phone

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecurePlainPhone":
        
        phone = String.read(b)
        
        return SecurePlainPhone(phone=phone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.phone))
        
        return b.getvalue()

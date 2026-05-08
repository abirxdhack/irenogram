
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CancelCode(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``1F040578``

    Parameters:
        phone_number (``str``):
            N/A

        phone_code_hash (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["phone_number", "phone_code_hash"]

    ID = 0x1f040578
    QUALNAME = "functions.auth.CancelCode"

    def __init__(self, *, phone_number: str, phone_code_hash: str) -> None:
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CancelCode":
        
        phone_number = String.read(b)
        
        phone_code_hash = String.read(b)
        
        return CancelCode(phone_number=phone_number, phone_code_hash=phone_code_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.phone_number))
        
        b.write(String(self.phone_code_hash))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ConfirmPhone(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``5F2178C3``

    Parameters:
        phone_code_hash (``str``):
            N/A

        phone_code (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["phone_code_hash", "phone_code"]

    ID = 0x5f2178c3
    QUALNAME = "functions.account.ConfirmPhone"

    def __init__(self, *, phone_code_hash: str, phone_code: str) -> None:
        self.phone_code_hash = phone_code_hash
        self.phone_code = phone_code

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConfirmPhone":
        
        phone_code_hash = String.read(b)
        
        phone_code = String.read(b)
        
        return ConfirmPhone(phone_code_hash=phone_code_hash, phone_code=phone_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.phone_code_hash))
        
        b.write(String(self.phone_code))
        
        return b.getvalue()

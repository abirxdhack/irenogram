
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ResetLoginEmail(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``7E960193``

    Parameters:
        phone_number (``str``):
            N/A

        phone_code_hash (``str``):
            N/A

    Returns:
        :obj:`auth.SentCode <pyrogram.raw.base.auth.SentCode>`
    """

    __slots__: List[str] = ["phone_number", "phone_code_hash"]

    ID = 0x7e960193
    QUALNAME = "functions.auth.ResetLoginEmail"

    def __init__(self, *, phone_number: str, phone_code_hash: str) -> None:
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResetLoginEmail":
        
        phone_number = String.read(b)
        
        phone_code_hash = String.read(b)
        
        return ResetLoginEmail(phone_number=phone_number, phone_code_hash=phone_code_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.phone_number))
        
        b.write(String(self.phone_code_hash))
        
        return b.getvalue()

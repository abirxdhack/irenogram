
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChangePhone(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``70C32EDB``

    Parameters:
        phone_number (``str``):
            N/A

        phone_code_hash (``str``):
            N/A

        phone_code (``str``):
            N/A

    Returns:
        :obj:`User <pyrogram.raw.base.User>`
    """

    __slots__: List[str] = ["phone_number", "phone_code_hash", "phone_code"]

    ID = 0x70c32edb
    QUALNAME = "functions.account.ChangePhone"

    def __init__(self, *, phone_number: str, phone_code_hash: str, phone_code: str) -> None:
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.phone_code = phone_code

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChangePhone":
        
        phone_number = String.read(b)
        
        phone_code_hash = String.read(b)
        
        phone_code = String.read(b)
        
        return ChangePhone(phone_number=phone_number, phone_code_hash=phone_code_hash, phone_code=phone_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.phone_number))
        
        b.write(String(self.phone_code_hash))
        
        b.write(String(self.phone_code))
        
        return b.getvalue()

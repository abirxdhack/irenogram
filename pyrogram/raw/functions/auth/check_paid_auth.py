
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CheckPaidAuth(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``56E59F9C``

    Parameters:
        phone_number (``str``):
            N/A

        phone_code_hash (``str``):
            N/A

        form_id (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`auth.SentCode <pyrogram.raw.base.auth.SentCode>`
    """

    __slots__: List[str] = ["phone_number", "phone_code_hash", "form_id"]

    ID = 0x56e59f9c
    QUALNAME = "functions.auth.CheckPaidAuth"

    def __init__(self, *, phone_number: str, phone_code_hash: str, form_id: int) -> None:
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.form_id = form_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckPaidAuth":
        
        phone_number = String.read(b)
        
        phone_code_hash = String.read(b)
        
        form_id = Long.read(b)
        
        return CheckPaidAuth(phone_number=phone_number, phone_code_hash=phone_code_hash, form_id=form_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.phone_number))
        
        b.write(String(self.phone_code_hash))
        
        b.write(Long(self.form_id))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ResendCode(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``CAE47523``

    Parameters:
        phone_number (``str``):
            N/A

        phone_code_hash (``str``):
            N/A

        reason (``str``, *optional*):
            N/A

    Returns:
        :obj:`auth.SentCode <pyrogram.raw.base.auth.SentCode>`
    """

    __slots__: List[str] = ["phone_number", "phone_code_hash", "reason"]

    ID = 0xcae47523
    QUALNAME = "functions.auth.ResendCode"

    def __init__(self, *, phone_number: str, phone_code_hash: str, reason: Optional[str] = None) -> None:
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.reason = reason

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResendCode":
        
        flags = Int.read(b)
        
        phone_number = String.read(b)
        
        phone_code_hash = String.read(b)
        
        reason = String.read(b) if flags & (1 << 0) else None
        return ResendCode(phone_number=phone_number, phone_code_hash=phone_code_hash, reason=reason)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.reason is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.phone_number))
        
        b.write(String(self.phone_code_hash))
        
        if self.reason is not None:
            b.write(String(self.reason))
        
        return b.getvalue()

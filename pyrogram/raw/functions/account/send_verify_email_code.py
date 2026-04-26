
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SendVerifyEmailCode(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``98E037BB``

    Parameters:
        purpose (:obj:`EmailVerifyPurpose <pyrogram.raw.base.EmailVerifyPurpose>`):
            N/A

        email (``str``):
            N/A

    Returns:
        :obj:`account.SentEmailCode <pyrogram.raw.base.account.SentEmailCode>`
    """

    __slots__: List[str] = ["purpose", "email"]

    ID = 0x98e037bb
    QUALNAME = "functions.account.SendVerifyEmailCode"

    def __init__(self, *, purpose: "raw.base.EmailVerifyPurpose", email: str) -> None:
        self.purpose = purpose
        self.email = email

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendVerifyEmailCode":
        
        purpose = TLObject.read(b)
        
        email = String.read(b)
        
        return SendVerifyEmailCode(purpose=purpose, email=email)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.purpose.write())
        
        b.write(String(self.email))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class VerifyEmail(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``32DA4CF``

    Parameters:
        purpose (:obj:`EmailVerifyPurpose <pyrogram.raw.base.EmailVerifyPurpose>`):
            N/A

        verification (:obj:`EmailVerification <pyrogram.raw.base.EmailVerification>`):
            N/A

    Returns:
        :obj:`account.EmailVerified <pyrogram.raw.base.account.EmailVerified>`
    """

    __slots__: List[str] = ["purpose", "verification"]

    ID = 0x32da4cf
    QUALNAME = "functions.account.VerifyEmail"

    def __init__(self, *, purpose: "raw.base.EmailVerifyPurpose", verification: "raw.base.EmailVerification") -> None:
        self.purpose = purpose
        self.verification = verification

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "VerifyEmail":
        
        purpose = TLObject.read(b)
        
        verification = TLObject.read(b)
        
        return VerifyEmail(purpose=purpose, verification=verification)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.purpose.write())
        
        b.write(self.verification.write())
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EmailVerificationApple(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.EmailVerification`.

    Details:
        - Layer: ``224``
        - ID: ``96D074FD``

    Parameters:
        token (``str``):
            N/A

    """

    __slots__: List[str] = ["token"]

    ID = 0x96d074fd
    QUALNAME = "types.EmailVerificationApple"

    def __init__(self, *, token: str) -> None:
        self.token = token

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmailVerificationApple":
        
        token = String.read(b)
        
        return EmailVerificationApple(token=token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.token))
        
        return b.getvalue()

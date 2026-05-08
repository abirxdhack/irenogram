
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CheckRecoveryPassword(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D36BF79``

    Parameters:
        code (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["code"]

    ID = 0xd36bf79
    QUALNAME = "functions.auth.CheckRecoveryPassword"

    def __init__(self, *, code: str) -> None:
        self.code = code

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckRecoveryPassword":
        
        code = String.read(b)
        
        return CheckRecoveryPassword(code=code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.code))
        
        return b.getvalue()

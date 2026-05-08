
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InvalidateSignInCodes(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``CA8AE8BA``

    Parameters:
        codes (List of ``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["codes"]

    ID = 0xca8ae8ba
    QUALNAME = "functions.account.InvalidateSignInCodes"

    def __init__(self, *, codes: List[str]) -> None:
        self.codes = codes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvalidateSignInCodes":
        
        codes = TLObject.read(b, String)
        
        return InvalidateSignInCodes(codes=codes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.codes, String))
        
        return b.getvalue()

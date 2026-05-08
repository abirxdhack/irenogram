
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ResetAuthorization(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``DF77F3BC``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["hash"]

    ID = 0xdf77f3bc
    QUALNAME = "functions.account.ResetAuthorization"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResetAuthorization":
        
        hash = Long.read(b)
        
        return ResetAuthorization(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        return b.getvalue()

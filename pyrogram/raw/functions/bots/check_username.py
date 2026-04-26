
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CheckUsername(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``87F2219B``

    Parameters:
        username (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["username"]

    ID = 0x87f2219b
    QUALNAME = "functions.bots.CheckUsername"

    def __init__(self, *, username: str) -> None:
        self.username = username

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckUsername":
        
        username = String.read(b)
        
        return CheckUsername(username=username)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.username))
        
        return b.getvalue()

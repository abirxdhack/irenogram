
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CheckShortName(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``284B3639``

    Parameters:
        short_name (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["short_name"]

    ID = 0x284b3639
    QUALNAME = "functions.stickers.CheckShortName"

    def __init__(self, *, short_name: str) -> None:
        self.short_name = short_name

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckShortName":
        
        short_name = String.read(b)
        
        return CheckShortName(short_name=short_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.short_name))
        
        return b.getvalue()

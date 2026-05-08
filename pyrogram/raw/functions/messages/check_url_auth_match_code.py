
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CheckUrlAuthMatchCode(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``C9A47B0B``

    Parameters:
        url (``str``):
            N/A

        match_code (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["url", "match_code"]

    ID = 0xc9a47b0b
    QUALNAME = "functions.messages.CheckUrlAuthMatchCode"

    def __init__(self, *, url: str, match_code: str) -> None:
        self.url = url
        self.match_code = match_code

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckUrlAuthMatchCode":
        
        url = String.read(b)
        
        match_code = String.read(b)
        
        return CheckUrlAuthMatchCode(url=url, match_code=match_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.url))
        
        b.write(String(self.match_code))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DeclineUrlAuth(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``35436BBC``

    Parameters:
        url (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["url"]

    ID = 0x35436bbc
    QUALNAME = "functions.messages.DeclineUrlAuth"

    def __init__(self, *, url: str) -> None:
        self.url = url

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeclineUrlAuth":
        
        url = String.read(b)
        
        return DeclineUrlAuth(url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.url))
        
        return b.getvalue()

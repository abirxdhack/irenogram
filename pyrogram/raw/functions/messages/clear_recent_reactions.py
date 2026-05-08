
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ClearRecentReactions(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``9DFEEFB4``

    Parameters:
        No parameters required.

    Returns:
        ``bool``
    """

    __slots__: List[str] = []

    ID = 0x9dfeefb4
    QUALNAME = "functions.messages.ClearRecentReactions"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ClearRecentReactions":
        
        return ClearRecentReactions()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetQuickReplies(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D483F2A8``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`messages.QuickReplies <pyrogram.raw.base.messages.QuickReplies>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0xd483f2a8
    QUALNAME = "functions.messages.GetQuickReplies"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetQuickReplies":
        
        hash = Long.read(b)
        
        return GetQuickReplies(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        return b.getvalue()

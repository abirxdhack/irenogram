
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetBotUpdatesStatus(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``EC22CFCD``

    Parameters:
        pending_updates_count (``int`` ``32-bit``):
            N/A

        message (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["pending_updates_count", "message"]

    ID = 0xec22cfcd
    QUALNAME = "functions.help.SetBotUpdatesStatus"

    def __init__(self, *, pending_updates_count: int, message: str) -> None:
        self.pending_updates_count = pending_updates_count
        self.message = message

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetBotUpdatesStatus":
        
        pending_updates_count = Int.read(b)
        
        message = String.read(b)
        
        return SetBotUpdatesStatus(pending_updates_count=pending_updates_count, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.pending_updates_count))
        
        b.write(String(self.message))
        
        return b.getvalue()

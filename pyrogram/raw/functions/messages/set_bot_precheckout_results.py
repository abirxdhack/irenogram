
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetBotPrecheckoutResults(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``9C2DD95``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

        success (``bool``, *optional*):
            N/A

        error (``str``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["query_id", "success", "error"]

    ID = 0x9c2dd95
    QUALNAME = "functions.messages.SetBotPrecheckoutResults"

    def __init__(self, *, query_id: int, success: Optional[bool] = None, error: Optional[str] = None) -> None:
        self.query_id = query_id
        self.success = success
        self.error = error

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetBotPrecheckoutResults":
        
        flags = Int.read(b)
        
        success = True if flags & (1 << 1) else False
        query_id = Long.read(b)
        
        error = String.read(b) if flags & (1 << 0) else None
        return SetBotPrecheckoutResults(query_id=query_id, success=success, error=error)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.success else 0
        flags |= (1 << 0) if self.error is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        if self.error is not None:
            b.write(String(self.error))
        
        return b.getvalue()

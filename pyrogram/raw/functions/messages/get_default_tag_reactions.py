
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetDefaultTagReactions(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``BDF93428``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`messages.Reactions <pyrogram.raw.base.messages.Reactions>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0xbdf93428
    QUALNAME = "functions.messages.GetDefaultTagReactions"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDefaultTagReactions":
        
        hash = Long.read(b)
        
        return GetDefaultTagReactions(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetWallPapers(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``7967D36``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`account.WallPapers <pyrogram.raw.base.account.WallPapers>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x7967d36
    QUALNAME = "functions.account.GetWallPapers"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetWallPapers":
        
        hash = Long.read(b)
        
        return GetWallPapers(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        return b.getvalue()

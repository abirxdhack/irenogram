
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class WallPapers(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.WallPapers`.

    Details:
        - Layer: ``224``
        - ID: ``CDC3858C``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        wallpapers (List of :obj:`WallPaper <pyrogram.raw.base.WallPaper>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetWallPapers
    """

    __slots__: List[str] = ["hash", "wallpapers"]

    ID = 0xcdc3858c
    QUALNAME = "types.account.WallPapers"

    def __init__(self, *, hash: int, wallpapers: List["raw.base.WallPaper"]) -> None:
        self.hash = hash
        self.wallpapers = wallpapers

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WallPapers":
        
        hash = Long.read(b)
        
        wallpapers = TLObject.read(b)
        
        return WallPapers(hash=hash, wallpapers=wallpapers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        b.write(Vector(self.wallpapers))
        
        return b.getvalue()

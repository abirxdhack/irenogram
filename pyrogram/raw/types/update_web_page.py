
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateWebPage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``7F891213``

    Parameters:
        webpage (:obj:`WebPage <pyrogram.raw.base.WebPage>`):
            N/A

        pts (``int`` ``32-bit``):
            N/A

        pts_count (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["webpage", "pts", "pts_count"]

    ID = 0x7f891213
    QUALNAME = "types.UpdateWebPage"

    def __init__(self, *, webpage: "raw.base.WebPage", pts: int, pts_count: int) -> None:
        self.webpage = webpage
        self.pts = pts
        self.pts_count = pts_count

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateWebPage":
        
        webpage = TLObject.read(b)
        
        pts = Int.read(b)
        
        pts_count = Int.read(b)
        
        return UpdateWebPage(webpage=webpage, pts=pts, pts_count=pts_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.webpage.write())
        
        b.write(Int(self.pts))
        
        b.write(Int(self.pts_count))
        
        return b.getvalue()

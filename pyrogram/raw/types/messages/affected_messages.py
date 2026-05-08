
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AffectedMessages(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.AffectedMessages`.

    Details:
        - Layer: ``224``
        - ID: ``84D19185``

    Parameters:
        pts (``int`` ``32-bit``):
            N/A

        pts_count (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.ReadHistory
            messages.DeleteMessages
            messages.ReadMessageContents
            channels.DeleteMessages
    """

    __slots__: List[str] = ["pts", "pts_count"]

    ID = 0x84d19185
    QUALNAME = "types.messages.AffectedMessages"

    def __init__(self, *, pts: int, pts_count: int) -> None:
        self.pts = pts
        self.pts_count = pts_count

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AffectedMessages":
        
        pts = Int.read(b)
        
        pts_count = Int.read(b)
        
        return AffectedMessages(pts=pts, pts_count=pts_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.pts))
        
        b.write(Int(self.pts_count))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AffectedHistory(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.AffectedHistory`.

    Details:
        - Layer: ``224``
        - ID: ``B45C69D1``

    Parameters:
        pts (``int`` ``32-bit``):
            N/A

        pts_count (``int`` ``32-bit``):
            N/A

        offset (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 8 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.DeleteHistory
            messages.ReadMentions
            messages.UnpinAllMessages
            messages.ReadReactions
            messages.DeleteSavedHistory
            messages.DeleteTopicHistory
            messages.ReadPollVotes
            channels.DeleteParticipantHistory
    """

    __slots__: List[str] = ["pts", "pts_count", "offset"]

    ID = 0xb45c69d1
    QUALNAME = "types.messages.AffectedHistory"

    def __init__(self, *, pts: int, pts_count: int, offset: int) -> None:
        self.pts = pts
        self.pts_count = pts_count
        self.offset = offset

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AffectedHistory":
        
        pts = Int.read(b)
        
        pts_count = Int.read(b)
        
        offset = Int.read(b)
        
        return AffectedHistory(pts=pts, pts_count=pts_count, offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.pts))
        
        b.write(Int(self.pts_count))
        
        b.write(Int(self.offset))
        
        return b.getvalue()

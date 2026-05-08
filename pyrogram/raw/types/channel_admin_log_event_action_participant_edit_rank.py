
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionParticipantEditRank(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``5806B4EC``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        prev_rank (``str``):
            N/A

        new_rank (``str``):
            N/A

    """

    __slots__: List[str] = ["user_id", "prev_rank", "new_rank"]

    ID = 0x5806b4ec
    QUALNAME = "types.ChannelAdminLogEventActionParticipantEditRank"

    def __init__(self, *, user_id: int, prev_rank: str, new_rank: str) -> None:
        self.user_id = user_id
        self.prev_rank = prev_rank
        self.new_rank = new_rank

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionParticipantEditRank":
        
        user_id = Long.read(b)
        
        prev_rank = String.read(b)
        
        new_rank = String.read(b)
        
        return ChannelAdminLogEventActionParticipantEditRank(user_id=user_id, prev_rank=prev_rank, new_rank=new_rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.user_id))
        
        b.write(String(self.prev_rank))
        
        b.write(String(self.new_rank))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChatParticipantAdmin(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatParticipant`.

    Details:
        - Layer: ``224``
        - ID: ``360D5D2``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        inviter_id (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        rank (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["user_id", "inviter_id", "date", "rank"]

    ID = 0x360d5d2
    QUALNAME = "types.ChatParticipantAdmin"

    def __init__(self, *, user_id: int, inviter_id: int, date: int, rank: Optional[str] = None) -> None:
        self.user_id = user_id
        self.inviter_id = inviter_id
        self.date = date
        self.rank = rank

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatParticipantAdmin":
        
        flags = Int.read(b)
        
        user_id = Long.read(b)
        
        inviter_id = Long.read(b)
        
        date = Int.read(b)
        
        rank = String.read(b) if flags & (1 << 0) else None
        return ChatParticipantAdmin(user_id=user_id, inviter_id=inviter_id, date=date, rank=rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.rank is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        b.write(Long(self.inviter_id))
        
        b.write(Int(self.date))
        
        if self.rank is not None:
            b.write(String(self.rank))
        
        return b.getvalue()

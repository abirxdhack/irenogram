
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChatParticipantCreator(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatParticipant`.

    Details:
        - Layer: ``224``
        - ID: ``E1F867B8``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        rank (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["user_id", "rank"]

    ID = 0xe1f867b8
    QUALNAME = "types.ChatParticipantCreator"

    def __init__(self, *, user_id: int, rank: Optional[str] = None) -> None:
        self.user_id = user_id
        self.rank = rank

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatParticipantCreator":
        
        flags = Int.read(b)
        
        user_id = Long.read(b)
        
        rank = String.read(b) if flags & (1 << 0) else None
        return ChatParticipantCreator(user_id=user_id, rank=rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.rank is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        if self.rank is not None:
            b.write(String(self.rank))
        
        return b.getvalue()

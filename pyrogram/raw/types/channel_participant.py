
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelParticipant(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelParticipant`.

    Details:
        - Layer: ``224``
        - ID: ``1BD54456``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        subscription_until_date (``int`` ``32-bit``, *optional*):
            N/A

        rank (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["user_id", "date", "subscription_until_date", "rank"]

    ID = 0x1bd54456
    QUALNAME = "types.ChannelParticipant"

    def __init__(self, *, user_id: int, date: int, subscription_until_date: Optional[int] = None, rank: Optional[str] = None) -> None:
        self.user_id = user_id
        self.date = date
        self.subscription_until_date = subscription_until_date
        self.rank = rank

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipant":
        
        flags = Int.read(b)
        
        user_id = Long.read(b)
        
        date = Int.read(b)
        
        subscription_until_date = Int.read(b) if flags & (1 << 0) else None
        rank = String.read(b) if flags & (1 << 2) else None
        return ChannelParticipant(user_id=user_id, date=date, subscription_until_date=subscription_until_date, rank=rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.subscription_until_date is not None else 0
        flags |= (1 << 2) if self.rank is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        b.write(Int(self.date))
        
        if self.subscription_until_date is not None:
            b.write(Int(self.subscription_until_date))
        
        if self.rank is not None:
            b.write(String(self.rank))
        
        return b.getvalue()

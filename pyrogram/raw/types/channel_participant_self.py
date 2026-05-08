
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelParticipantSelf(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelParticipant`.

    Details:
        - Layer: ``224``
        - ID: ``A9478A1A``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        inviter_id (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        via_request (``bool``, *optional*):
            N/A

        subscription_until_date (``int`` ``32-bit``, *optional*):
            N/A

        rank (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["user_id", "inviter_id", "date", "via_request", "subscription_until_date", "rank"]

    ID = 0xa9478a1a
    QUALNAME = "types.ChannelParticipantSelf"

    def __init__(self, *, user_id: int, inviter_id: int, date: int, via_request: Optional[bool] = None, subscription_until_date: Optional[int] = None, rank: Optional[str] = None) -> None:
        self.user_id = user_id
        self.inviter_id = inviter_id
        self.date = date
        self.via_request = via_request
        self.subscription_until_date = subscription_until_date
        self.rank = rank

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipantSelf":
        
        flags = Int.read(b)
        
        via_request = True if flags & (1 << 0) else False
        user_id = Long.read(b)
        
        inviter_id = Long.read(b)
        
        date = Int.read(b)
        
        subscription_until_date = Int.read(b) if flags & (1 << 1) else None
        rank = String.read(b) if flags & (1 << 2) else None
        return ChannelParticipantSelf(user_id=user_id, inviter_id=inviter_id, date=date, via_request=via_request, subscription_until_date=subscription_until_date, rank=rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.via_request else 0
        flags |= (1 << 1) if self.subscription_until_date is not None else 0
        flags |= (1 << 2) if self.rank is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        b.write(Long(self.inviter_id))
        
        b.write(Int(self.date))
        
        if self.subscription_until_date is not None:
            b.write(Int(self.subscription_until_date))
        
        if self.rank is not None:
            b.write(String(self.rank))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PhoneCallDiscarded(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PhoneCall`.

    Details:
        - Layer: ``224``
        - ID: ``50CA4DE1``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        need_rating (``bool``, *optional*):
            N/A

        need_debug (``bool``, *optional*):
            N/A

        video (``bool``, *optional*):
            N/A

        reason (:obj:`PhoneCallDiscardReason <pyrogram.raw.base.PhoneCallDiscardReason>`, *optional*):
            N/A

        duration (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "need_rating", "need_debug", "video", "reason", "duration"]

    ID = 0x50ca4de1
    QUALNAME = "types.PhoneCallDiscarded"

    def __init__(self, *, id: int, need_rating: Optional[bool] = None, need_debug: Optional[bool] = None, video: Optional[bool] = None, reason: "raw.base.PhoneCallDiscardReason" = None, duration: Optional[int] = None) -> None:
        self.id = id
        self.need_rating = need_rating
        self.need_debug = need_debug
        self.video = video
        self.reason = reason
        self.duration = duration

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneCallDiscarded":
        
        flags = Int.read(b)
        
        need_rating = True if flags & (1 << 2) else False
        need_debug = True if flags & (1 << 3) else False
        video = True if flags & (1 << 6) else False
        id = Long.read(b)
        
        reason = TLObject.read(b) if flags & (1 << 0) else None
        
        duration = Int.read(b) if flags & (1 << 1) else None
        return PhoneCallDiscarded(id=id, need_rating=need_rating, need_debug=need_debug, video=video, reason=reason, duration=duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.need_rating else 0
        flags |= (1 << 3) if self.need_debug else 0
        flags |= (1 << 6) if self.video else 0
        flags |= (1 << 0) if self.reason is not None else 0
        flags |= (1 << 1) if self.duration is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        if self.reason is not None:
            b.write(self.reason.write())
        
        if self.duration is not None:
            b.write(Int(self.duration))
        
        return b.getvalue()

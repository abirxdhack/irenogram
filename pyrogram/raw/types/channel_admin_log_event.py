
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEvent(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEvent`.

    Details:
        - Layer: ``224``
        - ID: ``1FAD68CD``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        user_id (``int`` ``64-bit``):
            N/A

        action (:obj:`ChannelAdminLogEventAction <pyrogram.raw.base.ChannelAdminLogEventAction>`):
            N/A

    """

    __slots__: List[str] = ["id", "date", "user_id", "action"]

    ID = 0x1fad68cd
    QUALNAME = "types.ChannelAdminLogEvent"

    def __init__(self, *, id: int, date: int, user_id: int, action: "raw.base.ChannelAdminLogEventAction") -> None:
        self.id = id
        self.date = date
        self.user_id = user_id
        self.action = action

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEvent":
        
        id = Long.read(b)
        
        date = Int.read(b)
        
        user_id = Long.read(b)
        
        action = TLObject.read(b)
        
        return ChannelAdminLogEvent(id=id, date=date, user_id=user_id, action=action)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        
        b.write(Int(self.date))
        
        b.write(Long(self.user_id))
        
        b.write(self.action.write())
        
        return b.getvalue()

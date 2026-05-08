
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateBotStopped(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``C4870A49``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        stopped (``bool``):
            N/A

        qts (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["user_id", "date", "stopped", "qts"]

    ID = 0xc4870a49
    QUALNAME = "types.UpdateBotStopped"

    def __init__(self, *, user_id: int, date: int, stopped: bool, qts: int) -> None:
        self.user_id = user_id
        self.date = date
        self.stopped = stopped
        self.qts = qts

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotStopped":
        
        user_id = Long.read(b)
        
        date = Int.read(b)
        
        stopped = Bool.read(b)
        
        qts = Int.read(b)
        
        return UpdateBotStopped(user_id=user_id, date=date, stopped=stopped, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.user_id))
        
        b.write(Int(self.date))
        
        b.write(Bool(self.stopped))
        
        b.write(Int(self.qts))
        
        return b.getvalue()

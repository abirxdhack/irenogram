
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateManagedBot(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``4880ED9A``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        bot_id (``int`` ``64-bit``):
            N/A

        qts (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["user_id", "bot_id", "qts"]

    ID = 0x4880ed9a
    QUALNAME = "types.UpdateManagedBot"

    def __init__(self, *, user_id: int, bot_id: int, qts: int) -> None:
        self.user_id = user_id
        self.bot_id = bot_id
        self.qts = qts

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateManagedBot":
        
        user_id = Long.read(b)
        
        bot_id = Long.read(b)
        
        qts = Int.read(b)
        
        return UpdateManagedBot(user_id=user_id, bot_id=bot_id, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.user_id))
        
        b.write(Long(self.bot_id))
        
        b.write(Int(self.qts))
        
        return b.getvalue()

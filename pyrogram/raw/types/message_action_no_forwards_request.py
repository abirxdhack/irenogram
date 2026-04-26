
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageActionNoForwardsRequest(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``3E2793BA``

    Parameters:
        prev_value (``bool``):
            N/A

        new_value (``bool``):
            N/A

        expired (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["prev_value", "new_value", "expired"]

    ID = 0x3e2793ba
    QUALNAME = "types.MessageActionNoForwardsRequest"

    def __init__(self, *, prev_value: bool, new_value: bool, expired: Optional[bool] = None) -> None:
        self.prev_value = prev_value
        self.new_value = new_value
        self.expired = expired

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionNoForwardsRequest":
        
        flags = Int.read(b)
        
        expired = True if flags & (1 << 0) else False
        prev_value = Bool.read(b)
        
        new_value = Bool.read(b)
        
        return MessageActionNoForwardsRequest(prev_value=prev_value, new_value=new_value, expired=expired)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.expired else 0
        b.write(Int(flags))
        
        b.write(Bool(self.prev_value))
        
        b.write(Bool(self.new_value))
        
        return b.getvalue()

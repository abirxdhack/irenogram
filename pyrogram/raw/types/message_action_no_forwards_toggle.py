
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageActionNoForwardsToggle(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``BF7D6572``

    Parameters:
        prev_value (``bool``):
            N/A

        new_value (``bool``):
            N/A

    """

    __slots__: List[str] = ["prev_value", "new_value"]

    ID = 0xbf7d6572
    QUALNAME = "types.MessageActionNoForwardsToggle"

    def __init__(self, *, prev_value: bool, new_value: bool) -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionNoForwardsToggle":
        
        prev_value = Bool.read(b)
        
        new_value = Bool.read(b)
        
        return MessageActionNoForwardsToggle(prev_value=prev_value, new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Bool(self.prev_value))
        
        b.write(Bool(self.new_value))
        
        return b.getvalue()

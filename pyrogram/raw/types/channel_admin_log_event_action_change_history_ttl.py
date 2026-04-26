
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionChangeHistoryTTL(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``6E941A38``

    Parameters:
        prev_value (``int`` ``32-bit``):
            N/A

        new_value (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["prev_value", "new_value"]

    ID = 0x6e941a38
    QUALNAME = "types.ChannelAdminLogEventActionChangeHistoryTTL"

    def __init__(self, *, prev_value: int, new_value: int) -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangeHistoryTTL":
        
        prev_value = Int.read(b)
        
        new_value = Int.read(b)
        
        return ChannelAdminLogEventActionChangeHistoryTTL(prev_value=prev_value, new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.prev_value))
        
        b.write(Int(self.new_value))
        
        return b.getvalue()

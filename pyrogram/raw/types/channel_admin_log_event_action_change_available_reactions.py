
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionChangeAvailableReactions(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``BE4E0EF8``

    Parameters:
        prev_value (:obj:`ChatReactions <pyrogram.raw.base.ChatReactions>`):
            N/A

        new_value (:obj:`ChatReactions <pyrogram.raw.base.ChatReactions>`):
            N/A

    """

    __slots__: List[str] = ["prev_value", "new_value"]

    ID = 0xbe4e0ef8
    QUALNAME = "types.ChannelAdminLogEventActionChangeAvailableReactions"

    def __init__(self, *, prev_value: "raw.base.ChatReactions", new_value: "raw.base.ChatReactions") -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangeAvailableReactions":
        
        prev_value = TLObject.read(b)
        
        new_value = TLObject.read(b)
        
        return ChannelAdminLogEventActionChangeAvailableReactions(prev_value=prev_value, new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.prev_value.write())
        
        b.write(self.new_value.write())
        
        return b.getvalue()

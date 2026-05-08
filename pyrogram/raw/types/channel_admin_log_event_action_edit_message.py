
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionEditMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``709B2405``

    Parameters:
        prev_message (:obj:`Message <pyrogram.raw.base.Message>`):
            N/A

        new_message (:obj:`Message <pyrogram.raw.base.Message>`):
            N/A

    """

    __slots__: List[str] = ["prev_message", "new_message"]

    ID = 0x709b2405
    QUALNAME = "types.ChannelAdminLogEventActionEditMessage"

    def __init__(self, *, prev_message: "raw.base.Message", new_message: "raw.base.Message") -> None:
        self.prev_message = prev_message
        self.new_message = new_message

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionEditMessage":
        
        prev_message = TLObject.read(b)
        
        new_message = TLObject.read(b)
        
        return ChannelAdminLogEventActionEditMessage(prev_message=prev_message, new_message=new_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.prev_message.write())
        
        b.write(self.new_message.write())
        
        return b.getvalue()

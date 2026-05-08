
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionSendMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``278F2868``

    Parameters:
        message (:obj:`Message <pyrogram.raw.base.Message>`):
            N/A

    """

    __slots__: List[str] = ["message"]

    ID = 0x278f2868
    QUALNAME = "types.ChannelAdminLogEventActionSendMessage"

    def __init__(self, *, message: "raw.base.Message") -> None:
        self.message = message

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionSendMessage":
        
        message = TLObject.read(b)
        
        return ChannelAdminLogEventActionSendMessage(message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.message.write())
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionChangeAbout(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``55188A2E``

    Parameters:
        prev_value (``str``):
            N/A

        new_value (``str``):
            N/A

    """

    __slots__: List[str] = ["prev_value", "new_value"]

    ID = 0x55188a2e
    QUALNAME = "types.ChannelAdminLogEventActionChangeAbout"

    def __init__(self, *, prev_value: str, new_value: str) -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangeAbout":
        
        prev_value = String.read(b)
        
        new_value = String.read(b)
        
        return ChannelAdminLogEventActionChangeAbout(prev_value=prev_value, new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.prev_value))
        
        b.write(String(self.new_value))
        
        return b.getvalue()

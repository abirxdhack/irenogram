
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionChangeLocation(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``E6B76AE``

    Parameters:
        prev_value (:obj:`ChannelLocation <pyrogram.raw.base.ChannelLocation>`):
            N/A

        new_value (:obj:`ChannelLocation <pyrogram.raw.base.ChannelLocation>`):
            N/A

    """

    __slots__: List[str] = ["prev_value", "new_value"]

    ID = 0xe6b76ae
    QUALNAME = "types.ChannelAdminLogEventActionChangeLocation"

    def __init__(self, *, prev_value: "raw.base.ChannelLocation", new_value: "raw.base.ChannelLocation") -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangeLocation":
        
        prev_value = TLObject.read(b)
        
        new_value = TLObject.read(b)
        
        return ChannelAdminLogEventActionChangeLocation(prev_value=prev_value, new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.prev_value.write())
        
        b.write(self.new_value.write())
        
        return b.getvalue()

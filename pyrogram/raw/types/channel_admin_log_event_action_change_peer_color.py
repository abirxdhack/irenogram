
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionChangePeerColor(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``5796E780``

    Parameters:
        prev_value (:obj:`PeerColor <pyrogram.raw.base.PeerColor>`):
            N/A

        new_value (:obj:`PeerColor <pyrogram.raw.base.PeerColor>`):
            N/A

    """

    __slots__: List[str] = ["prev_value", "new_value"]

    ID = 0x5796e780
    QUALNAME = "types.ChannelAdminLogEventActionChangePeerColor"

    def __init__(self, *, prev_value: "raw.base.PeerColor", new_value: "raw.base.PeerColor") -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangePeerColor":
        
        prev_value = TLObject.read(b)
        
        new_value = TLObject.read(b)
        
        return ChannelAdminLogEventActionChangePeerColor(prev_value=prev_value, new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.prev_value.write())
        
        b.write(self.new_value.write())
        
        return b.getvalue()

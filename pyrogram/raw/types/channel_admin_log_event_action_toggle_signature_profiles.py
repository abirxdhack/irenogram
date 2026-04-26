
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionToggleSignatureProfiles(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``60A79C79``

    Parameters:
        new_value (``bool``):
            N/A

    """

    __slots__: List[str] = ["new_value"]

    ID = 0x60a79c79
    QUALNAME = "types.ChannelAdminLogEventActionToggleSignatureProfiles"

    def __init__(self, *, new_value: bool) -> None:
        self.new_value = new_value

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionToggleSignatureProfiles":
        
        new_value = Bool.read(b)
        
        return ChannelAdminLogEventActionToggleSignatureProfiles(new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Bool(self.new_value))
        
        return b.getvalue()

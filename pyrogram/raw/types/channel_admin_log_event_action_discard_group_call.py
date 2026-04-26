
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionDiscardGroupCall(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``DB9F9140``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

    """

    __slots__: List[str] = ["call"]

    ID = 0xdb9f9140
    QUALNAME = "types.ChannelAdminLogEventActionDiscardGroupCall"

    def __init__(self, *, call: "raw.base.InputGroupCall") -> None:
        self.call = call

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionDiscardGroupCall":
        
        call = TLObject.read(b)
        
        return ChannelAdminLogEventActionDiscardGroupCall(call=call)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.call.write())
        
        return b.getvalue()

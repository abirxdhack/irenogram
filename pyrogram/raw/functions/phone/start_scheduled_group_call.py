
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StartScheduledGroupCall(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``5680E342``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call"]

    ID = 0x5680e342
    QUALNAME = "functions.phone.StartScheduledGroupCall"

    def __init__(self, *, call: "raw.base.InputGroupCall") -> None:
        self.call = call

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StartScheduledGroupCall":
        
        call = TLObject.read(b)
        
        return StartScheduledGroupCall(call=call)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.call.write())
        
        return b.getvalue()

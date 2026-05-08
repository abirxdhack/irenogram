
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class LeaveGroupCallPresentation(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``1C50D144``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call"]

    ID = 0x1c50d144
    QUALNAME = "functions.phone.LeaveGroupCallPresentation"

    def __init__(self, *, call: "raw.base.InputGroupCall") -> None:
        self.call = call

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LeaveGroupCallPresentation":
        
        call = TLObject.read(b)
        
        return LeaveGroupCallPresentation(call=call)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.call.write())
        
        return b.getvalue()

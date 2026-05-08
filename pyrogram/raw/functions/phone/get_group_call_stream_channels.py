
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetGroupCallStreamChannels(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``1AB21940``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

    Returns:
        :obj:`phone.GroupCallStreamChannels <pyrogram.raw.base.phone.GroupCallStreamChannels>`
    """

    __slots__: List[str] = ["call"]

    ID = 0x1ab21940
    QUALNAME = "functions.phone.GetGroupCallStreamChannels"

    def __init__(self, *, call: "raw.base.InputGroupCall") -> None:
        self.call = call

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGroupCallStreamChannels":
        
        call = TLObject.read(b)
        
        return GetGroupCallStreamChannels(call=call)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.call.write())
        
        return b.getvalue()

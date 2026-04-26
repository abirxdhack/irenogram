
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetGroupCallStars(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``6F636302``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

    Returns:
        :obj:`phone.GroupCallStars <pyrogram.raw.base.phone.GroupCallStars>`
    """

    __slots__: List[str] = ["call"]

    ID = 0x6f636302
    QUALNAME = "functions.phone.GetGroupCallStars"

    def __init__(self, *, call: "raw.base.InputGroupCall") -> None:
        self.call = call

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGroupCallStars":
        
        call = TLObject.read(b)
        
        return GetGroupCallStars(call=call)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.call.write())
        
        return b.getvalue()

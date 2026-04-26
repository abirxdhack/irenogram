
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetGroupCall(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``41845DB``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        limit (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`phone.GroupCall <pyrogram.raw.base.phone.GroupCall>`
    """

    __slots__: List[str] = ["call", "limit"]

    ID = 0x41845db
    QUALNAME = "functions.phone.GetGroupCall"

    def __init__(self, *, call: "raw.base.InputGroupCall", limit: int) -> None:
        self.call = call
        self.limit = limit

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGroupCall":
        
        call = TLObject.read(b)
        
        limit = Int.read(b)
        
        return GetGroupCall(call=call, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.call.write())
        
        b.write(Int(self.limit))
        
        return b.getvalue()

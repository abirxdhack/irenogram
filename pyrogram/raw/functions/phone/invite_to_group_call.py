
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InviteToGroupCall(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``7B393160``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        users (List of :obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "users"]

    ID = 0x7b393160
    QUALNAME = "functions.phone.InviteToGroupCall"

    def __init__(self, *, call: "raw.base.InputGroupCall", users: List["raw.base.InputUser"]) -> None:
        self.call = call
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InviteToGroupCall":
        
        call = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return InviteToGroupCall(call=call, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.call.write())
        
        b.write(Vector(self.users))
        
        return b.getvalue()

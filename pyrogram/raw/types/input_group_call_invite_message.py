
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputGroupCallInviteMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputGroupCall`.

    Details:
        - Layer: ``224``
        - ID: ``8C10603F``

    Parameters:
        msg_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["msg_id"]

    ID = 0x8c10603f
    QUALNAME = "types.InputGroupCallInviteMessage"

    def __init__(self, *, msg_id: int) -> None:
        self.msg_id = msg_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputGroupCallInviteMessage":
        
        msg_id = Int.read(b)
        
        return InputGroupCallInviteMessage(msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.msg_id))
        
        return b.getvalue()

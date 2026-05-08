
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DeclineConferenceCallInvite(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``3C479971``

    Parameters:
        msg_id (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["msg_id"]

    ID = 0x3c479971
    QUALNAME = "functions.phone.DeclineConferenceCallInvite"

    def __init__(self, *, msg_id: int) -> None:
        self.msg_id = msg_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeclineConferenceCallInvite":
        
        msg_id = Int.read(b)
        
        return DeclineConferenceCallInvite(msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.msg_id))
        
        return b.getvalue()

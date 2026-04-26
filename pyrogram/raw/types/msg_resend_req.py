
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MsgResendReq(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MsgResendReq`.

    Details:
        - Layer: ``224``
        - ID: ``7D861A08``

    Parameters:
        msg_ids (List of ``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["msg_ids"]

    ID = 0x7d861a08
    QUALNAME = "types.MsgResendReq"

    def __init__(self, *, msg_ids: List[int]) -> None:
        self.msg_ids = msg_ids

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MsgResendReq":
        
        msg_ids = TLObject.read(b, Long)
        
        return MsgResendReq(msg_ids=msg_ids)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.msg_ids, Long))
        
        return b.getvalue()

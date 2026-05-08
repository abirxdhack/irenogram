
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RpcDropAnswer(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``58E4A740``

    Parameters:
        req_msg_id (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`RpcDropAnswer <pyrogram.raw.base.RpcDropAnswer>`
    """

    __slots__: List[str] = ["req_msg_id"]

    ID = 0x58e4a740
    QUALNAME = "functions.RpcDropAnswer"

    def __init__(self, *, req_msg_id: int) -> None:
        self.req_msg_id = req_msg_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RpcDropAnswer":
        
        req_msg_id = Long.read(b)
        
        return RpcDropAnswer(req_msg_id=req_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.req_msg_id))
        
        return b.getvalue()

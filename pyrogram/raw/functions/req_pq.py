
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReqPq(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``60469778``

    Parameters:
        nonce (``int`` ``128-bit``):
            N/A

    Returns:
        :obj:`ResPQ <pyrogram.raw.base.ResPQ>`
    """

    __slots__: List[str] = ["nonce"]

    ID = 0x60469778
    QUALNAME = "functions.ReqPq"

    def __init__(self, *, nonce: int) -> None:
        self.nonce = nonce

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReqPq":
        
        nonce = Int128.read(b)
        
        return ReqPq(nonce=nonce)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int128(self.nonce))
        
        return b.getvalue()

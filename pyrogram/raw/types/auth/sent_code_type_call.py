
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SentCodeTypeCall(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.auth.SentCodeType`.

    Details:
        - Layer: ``224``
        - ID: ``5353E5A7``

    Parameters:
        length (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["length"]

    ID = 0x5353e5a7
    QUALNAME = "types.auth.SentCodeTypeCall"

    def __init__(self, *, length: int) -> None:
        self.length = length

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeCall":
        
        length = Int.read(b)
        
        return SentCodeTypeCall(length=length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.length))
        
        return b.getvalue()

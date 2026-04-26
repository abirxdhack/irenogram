
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SentCodeTypeApp(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.auth.SentCodeType`.

    Details:
        - Layer: ``224``
        - ID: ``3DBB5986``

    Parameters:
        length (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["length"]

    ID = 0x3dbb5986
    QUALNAME = "types.auth.SentCodeTypeApp"

    def __init__(self, *, length: int) -> None:
        self.length = length

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeApp":
        
        length = Int.read(b)
        
        return SentCodeTypeApp(length=length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.length))
        
        return b.getvalue()

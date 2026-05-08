
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SecureRequiredTypeOneOf(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SecureRequiredType`.

    Details:
        - Layer: ``224``
        - ID: ``27477B4``

    Parameters:
        types (List of :obj:`SecureRequiredType <pyrogram.raw.base.SecureRequiredType>`):
            N/A

    """

    __slots__: List[str] = ["types"]

    ID = 0x27477b4
    QUALNAME = "types.SecureRequiredTypeOneOf"

    def __init__(self, *, types: List["raw.base.SecureRequiredType"]) -> None:
        self.types = types

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureRequiredTypeOneOf":
        
        types = TLObject.read(b)
        
        return SecureRequiredTypeOneOf(types=types)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.types))
        
        return b.getvalue()

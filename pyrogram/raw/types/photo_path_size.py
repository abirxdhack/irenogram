
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PhotoPathSize(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PhotoSize`.

    Details:
        - Layer: ``224``
        - ID: ``D8214D41``

    Parameters:
        type (``str``):
            N/A

        bytes (``bytes``):
            N/A

    """

    __slots__: List[str] = ["type", "bytes"]

    ID = 0xd8214d41
    QUALNAME = "types.PhotoPathSize"

    def __init__(self, *, type: str, bytes: bytes) -> None:
        self.type = type
        self.bytes = bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhotoPathSize":
        
        type = String.read(b)
        
        bytes = Bytes.read(b)
        
        return PhotoPathSize(type=type, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.type))
        
        b.write(Bytes(self.bytes))
        
        return b.getvalue()

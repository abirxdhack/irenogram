
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PhotoSizeEmpty(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PhotoSize`.

    Details:
        - Layer: ``224``
        - ID: ``E17E23C``

    Parameters:
        type (``str``):
            N/A

    """

    __slots__: List[str] = ["type"]

    ID = 0xe17e23c
    QUALNAME = "types.PhotoSizeEmpty"

    def __init__(self, *, type: str) -> None:
        self.type = type

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhotoSizeEmpty":
        
        type = String.read(b)
        
        return PhotoSizeEmpty(type=type)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.type))
        
        return b.getvalue()

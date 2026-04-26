
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputStickerSetShortName(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputStickerSet`.

    Details:
        - Layer: ``224``
        - ID: ``861CC8A0``

    Parameters:
        short_name (``str``):
            N/A

    """

    __slots__: List[str] = ["short_name"]

    ID = 0x861cc8a0
    QUALNAME = "types.InputStickerSetShortName"

    def __init__(self, *, short_name: str) -> None:
        self.short_name = short_name

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStickerSetShortName":
        
        short_name = String.read(b)
        
        return InputStickerSetShortName(short_name=short_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.short_name))
        
        return b.getvalue()

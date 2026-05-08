
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateStoriesStealthMode(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``2C084DC1``

    Parameters:
        stealth_mode (:obj:`StoriesStealthMode <pyrogram.raw.base.StoriesStealthMode>`):
            N/A

    """

    __slots__: List[str] = ["stealth_mode"]

    ID = 0x2c084dc1
    QUALNAME = "types.UpdateStoriesStealthMode"

    def __init__(self, *, stealth_mode: "raw.base.StoriesStealthMode") -> None:
        self.stealth_mode = stealth_mode

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStoriesStealthMode":
        
        stealth_mode = TLObject.read(b)
        
        return UpdateStoriesStealthMode(stealth_mode=stealth_mode)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.stealth_mode.write())
        
        return b.getvalue()

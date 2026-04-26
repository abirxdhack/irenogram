
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RemoveStickerFromSet(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``F7760F51``

    Parameters:
        sticker (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            N/A

    Returns:
        :obj:`messages.StickerSet <pyrogram.raw.base.messages.StickerSet>`
    """

    __slots__: List[str] = ["sticker"]

    ID = 0xf7760f51
    QUALNAME = "functions.stickers.RemoveStickerFromSet"

    def __init__(self, *, sticker: "raw.base.InputDocument") -> None:
        self.sticker = sticker

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RemoveStickerFromSet":
        
        sticker = TLObject.read(b)
        
        return RemoveStickerFromSet(sticker=sticker)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.sticker.write())
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChangeStickerPosition(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``FFB6D4CA``

    Parameters:
        sticker (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            N/A

        position (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.StickerSet <pyrogram.raw.base.messages.StickerSet>`
    """

    __slots__: List[str] = ["sticker", "position"]

    ID = 0xffb6d4ca
    QUALNAME = "functions.stickers.ChangeStickerPosition"

    def __init__(self, *, sticker: "raw.base.InputDocument", position: int) -> None:
        self.sticker = sticker
        self.position = position

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChangeStickerPosition":
        
        sticker = TLObject.read(b)
        
        position = Int.read(b)
        
        return ChangeStickerPosition(sticker=sticker, position=position)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.sticker.write())
        
        b.write(Int(self.position))
        
        return b.getvalue()

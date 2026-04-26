
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class VideoSizeStickerMarkup(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.VideoSize`.

    Details:
        - Layer: ``224``
        - ID: ``DA082FE``

    Parameters:
        stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            N/A

        sticker_id (``int`` ``64-bit``):
            N/A

        background_colors (List of ``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["stickerset", "sticker_id", "background_colors"]

    ID = 0xda082fe
    QUALNAME = "types.VideoSizeStickerMarkup"

    def __init__(self, *, stickerset: "raw.base.InputStickerSet", sticker_id: int, background_colors: List[int]) -> None:
        self.stickerset = stickerset
        self.sticker_id = sticker_id
        self.background_colors = background_colors

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "VideoSizeStickerMarkup":
        
        stickerset = TLObject.read(b)
        
        sticker_id = Long.read(b)
        
        background_colors = TLObject.read(b, Int)
        
        return VideoSizeStickerMarkup(stickerset=stickerset, sticker_id=sticker_id, background_colors=background_colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.stickerset.write())
        
        b.write(Long(self.sticker_id))
        
        b.write(Vector(self.background_colors, Int))
        
        return b.getvalue()

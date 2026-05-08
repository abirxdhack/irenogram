
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DocumentAttributeCustomEmoji(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DocumentAttribute`.

    Details:
        - Layer: ``224``
        - ID: ``FD149899``

    Parameters:
        alt (``str``):
            N/A

        stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            N/A

        free (``bool``, *optional*):
            N/A

        text_color (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["alt", "stickerset", "free", "text_color"]

    ID = 0xfd149899
    QUALNAME = "types.DocumentAttributeCustomEmoji"

    def __init__(self, *, alt: str, stickerset: "raw.base.InputStickerSet", free: Optional[bool] = None, text_color: Optional[bool] = None) -> None:
        self.alt = alt
        self.stickerset = stickerset
        self.free = free
        self.text_color = text_color

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeCustomEmoji":
        
        flags = Int.read(b)
        
        free = True if flags & (1 << 0) else False
        text_color = True if flags & (1 << 1) else False
        alt = String.read(b)
        
        stickerset = TLObject.read(b)
        
        return DocumentAttributeCustomEmoji(alt=alt, stickerset=stickerset, free=free, text_color=text_color)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.free else 0
        flags |= (1 << 1) if self.text_color else 0
        b.write(Int(flags))
        
        b.write(String(self.alt))
        
        b.write(self.stickerset.write())
        
        return b.getvalue()

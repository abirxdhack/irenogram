
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class VideoSizeEmojiMarkup(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.VideoSize`.

    Details:
        - Layer: ``224``
        - ID: ``F85C413C``

    Parameters:
        emoji_id (``int`` ``64-bit``):
            N/A

        background_colors (List of ``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["emoji_id", "background_colors"]

    ID = 0xf85c413c
    QUALNAME = "types.VideoSizeEmojiMarkup"

    def __init__(self, *, emoji_id: int, background_colors: List[int]) -> None:
        self.emoji_id = emoji_id
        self.background_colors = background_colors

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "VideoSizeEmojiMarkup":
        
        emoji_id = Long.read(b)
        
        background_colors = TLObject.read(b, Int)
        
        return VideoSizeEmojiMarkup(emoji_id=emoji_id, background_colors=background_colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.emoji_id))
        
        b.write(Vector(self.background_colors, Int))
        
        return b.getvalue()

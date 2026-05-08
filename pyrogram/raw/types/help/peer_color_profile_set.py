
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PeerColorProfileSet(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.PeerColorSet`.

    Details:
        - Layer: ``224``
        - ID: ``767D61EB``

    Parameters:
        palette_colors (List of ``int`` ``32-bit``):
            N/A

        bg_colors (List of ``int`` ``32-bit``):
            N/A

        story_colors (List of ``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["palette_colors", "bg_colors", "story_colors"]

    ID = 0x767d61eb
    QUALNAME = "types.help.PeerColorProfileSet"

    def __init__(self, *, palette_colors: List[int], bg_colors: List[int], story_colors: List[int]) -> None:
        self.palette_colors = palette_colors
        self.bg_colors = bg_colors
        self.story_colors = story_colors

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerColorProfileSet":
        
        palette_colors = TLObject.read(b, Int)
        
        bg_colors = TLObject.read(b, Int)
        
        story_colors = TLObject.read(b, Int)
        
        return PeerColorProfileSet(palette_colors=palette_colors, bg_colors=bg_colors, story_colors=story_colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.palette_colors, Int))
        
        b.write(Vector(self.bg_colors, Int))
        
        b.write(Vector(self.story_colors, Int))
        
        return b.getvalue()

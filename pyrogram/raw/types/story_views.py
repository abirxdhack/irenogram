
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StoryViews(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StoryViews`.

    Details:
        - Layer: ``224``
        - ID: ``8D595CD6``

    Parameters:
        views_count (``int`` ``32-bit``):
            N/A

        has_viewers (``bool``, *optional*):
            N/A

        forwards_count (``int`` ``32-bit``, *optional*):
            N/A

        reactions (List of :obj:`ReactionCount <pyrogram.raw.base.ReactionCount>`, *optional*):
            N/A

        reactions_count (``int`` ``32-bit``, *optional*):
            N/A

        recent_viewers (List of ``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["views_count", "has_viewers", "forwards_count", "reactions", "reactions_count", "recent_viewers"]

    ID = 0x8d595cd6
    QUALNAME = "types.StoryViews"

    def __init__(self, *, views_count: int, has_viewers: Optional[bool] = None, forwards_count: Optional[int] = None, reactions: Optional[List["raw.base.ReactionCount"]] = None, reactions_count: Optional[int] = None, recent_viewers: Optional[List[int]] = None) -> None:
        self.views_count = views_count
        self.has_viewers = has_viewers
        self.forwards_count = forwards_count
        self.reactions = reactions
        self.reactions_count = reactions_count
        self.recent_viewers = recent_viewers

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryViews":
        
        flags = Int.read(b)
        
        has_viewers = True if flags & (1 << 1) else False
        views_count = Int.read(b)
        
        forwards_count = Int.read(b) if flags & (1 << 2) else None
        reactions = TLObject.read(b) if flags & (1 << 3) else []
        
        reactions_count = Int.read(b) if flags & (1 << 4) else None
        recent_viewers = TLObject.read(b, Long) if flags & (1 << 0) else []
        
        return StoryViews(views_count=views_count, has_viewers=has_viewers, forwards_count=forwards_count, reactions=reactions, reactions_count=reactions_count, recent_viewers=recent_viewers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.has_viewers else 0
        flags |= (1 << 2) if self.forwards_count is not None else 0
        flags |= (1 << 3) if self.reactions else 0
        flags |= (1 << 4) if self.reactions_count is not None else 0
        flags |= (1 << 0) if self.recent_viewers else 0
        b.write(Int(flags))
        
        b.write(Int(self.views_count))
        
        if self.forwards_count is not None:
            b.write(Int(self.forwards_count))
        
        if self.reactions is not None:
            b.write(Vector(self.reactions))
        
        if self.reactions_count is not None:
            b.write(Int(self.reactions_count))
        
        if self.recent_viewers is not None:
            b.write(Vector(self.recent_viewers, Long))
        
        return b.getvalue()

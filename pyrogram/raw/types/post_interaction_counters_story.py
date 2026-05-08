
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PostInteractionCountersStory(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PostInteractionCounters`.

    Details:
        - Layer: ``224``
        - ID: ``8A480E27``

    Parameters:
        story_id (``int`` ``32-bit``):
            N/A

        views (``int`` ``32-bit``):
            N/A

        forwards (``int`` ``32-bit``):
            N/A

        reactions (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["story_id", "views", "forwards", "reactions"]

    ID = 0x8a480e27
    QUALNAME = "types.PostInteractionCountersStory"

    def __init__(self, *, story_id: int, views: int, forwards: int, reactions: int) -> None:
        self.story_id = story_id
        self.views = views
        self.forwards = forwards
        self.reactions = reactions

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PostInteractionCountersStory":
        
        story_id = Int.read(b)
        
        views = Int.read(b)
        
        forwards = Int.read(b)
        
        reactions = Int.read(b)
        
        return PostInteractionCountersStory(story_id=story_id, views=views, forwards=forwards, reactions=reactions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.story_id))
        
        b.write(Int(self.views))
        
        b.write(Int(self.forwards))
        
        b.write(Int(self.reactions))
        
        return b.getvalue()

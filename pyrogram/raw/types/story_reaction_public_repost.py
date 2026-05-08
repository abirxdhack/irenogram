
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StoryReactionPublicRepost(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StoryReaction`.

    Details:
        - Layer: ``224``
        - ID: ``CFCD0F13``

    Parameters:
        peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        story (:obj:`StoryItem <pyrogram.raw.base.StoryItem>`):
            N/A

    """

    __slots__: List[str] = ["peer_id", "story"]

    ID = 0xcfcd0f13
    QUALNAME = "types.StoryReactionPublicRepost"

    def __init__(self, *, peer_id: "raw.base.Peer", story: "raw.base.StoryItem") -> None:
        self.peer_id = peer_id
        self.story = story

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryReactionPublicRepost":
        
        peer_id = TLObject.read(b)
        
        story = TLObject.read(b)
        
        return StoryReactionPublicRepost(peer_id=peer_id, story=story)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer_id.write())
        
        b.write(self.story.write())
        
        return b.getvalue()

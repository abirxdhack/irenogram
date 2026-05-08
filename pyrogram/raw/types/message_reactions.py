
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageReactions(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageReactions`.

    Details:
        - Layer: ``224``
        - ID: ``A339F0B``

    Parameters:
        results (List of :obj:`ReactionCount <pyrogram.raw.base.ReactionCount>`):
            N/A

        min (``bool``, *optional*):
            N/A

        can_see_list (``bool``, *optional*):
            N/A

        reactions_as_tags (``bool``, *optional*):
            N/A

        recent_reactions (List of :obj:`MessagePeerReaction <pyrogram.raw.base.MessagePeerReaction>`, *optional*):
            N/A

        top_reactors (List of :obj:`MessageReactor <pyrogram.raw.base.MessageReactor>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["results", "min", "can_see_list", "reactions_as_tags", "recent_reactions", "top_reactors"]

    ID = 0xa339f0b
    QUALNAME = "types.MessageReactions"

    def __init__(self, *, results: List["raw.base.ReactionCount"], min: Optional[bool] = None, can_see_list: Optional[bool] = None, reactions_as_tags: Optional[bool] = None, recent_reactions: Optional[List["raw.base.MessagePeerReaction"]] = None, top_reactors: Optional[List["raw.base.MessageReactor"]] = None) -> None:
        self.results = results
        self.min = min
        self.can_see_list = can_see_list
        self.reactions_as_tags = reactions_as_tags
        self.recent_reactions = recent_reactions
        self.top_reactors = top_reactors

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageReactions":
        
        flags = Int.read(b)
        
        min = True if flags & (1 << 0) else False
        can_see_list = True if flags & (1 << 2) else False
        reactions_as_tags = True if flags & (1 << 3) else False
        results = TLObject.read(b)
        
        recent_reactions = TLObject.read(b) if flags & (1 << 1) else []
        
        top_reactors = TLObject.read(b) if flags & (1 << 4) else []
        
        return MessageReactions(results=results, min=min, can_see_list=can_see_list, reactions_as_tags=reactions_as_tags, recent_reactions=recent_reactions, top_reactors=top_reactors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.min else 0
        flags |= (1 << 2) if self.can_see_list else 0
        flags |= (1 << 3) if self.reactions_as_tags else 0
        flags |= (1 << 1) if self.recent_reactions else 0
        flags |= (1 << 4) if self.top_reactors else 0
        b.write(Int(flags))
        
        b.write(Vector(self.results))
        
        if self.recent_reactions is not None:
            b.write(Vector(self.recent_reactions))
        
        if self.top_reactors is not None:
            b.write(Vector(self.top_reactors))
        
        return b.getvalue()

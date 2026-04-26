
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetStoryReactionsList(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``B9B2881F``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        id (``int`` ``32-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        forwards_first (``bool``, *optional*):
            N/A

        reaction (:obj:`Reaction <pyrogram.raw.base.Reaction>`, *optional*):
            N/A

        offset (``str``, *optional*):
            N/A

    Returns:
        :obj:`stories.StoryReactionsList <pyrogram.raw.base.stories.StoryReactionsList>`
    """

    __slots__: List[str] = ["peer", "id", "limit", "forwards_first", "reaction", "offset"]

    ID = 0xb9b2881f
    QUALNAME = "functions.stories.GetStoryReactionsList"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, limit: int, forwards_first: Optional[bool] = None, reaction: "raw.base.Reaction" = None, offset: Optional[str] = None) -> None:
        self.peer = peer
        self.id = id
        self.limit = limit
        self.forwards_first = forwards_first
        self.reaction = reaction
        self.offset = offset

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStoryReactionsList":
        
        flags = Int.read(b)
        
        forwards_first = True if flags & (1 << 2) else False
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        reaction = TLObject.read(b) if flags & (1 << 0) else None
        
        offset = String.read(b) if flags & (1 << 1) else None
        limit = Int.read(b)
        
        return GetStoryReactionsList(peer=peer, id=id, limit=limit, forwards_first=forwards_first, reaction=reaction, offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.forwards_first else 0
        flags |= (1 << 0) if self.reaction is not None else 0
        flags |= (1 << 1) if self.offset is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        if self.reaction is not None:
            b.write(self.reaction.write())
        
        if self.offset is not None:
            b.write(String(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PeerStories(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PeerStories`.

    Details:
        - Layer: ``224``
        - ID: ``9A35E999``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        stories (List of :obj:`StoryItem <pyrogram.raw.base.StoryItem>`):
            N/A

        max_read_id (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "stories", "max_read_id"]

    ID = 0x9a35e999
    QUALNAME = "types.PeerStories"

    def __init__(self, *, peer: "raw.base.Peer", stories: List["raw.base.StoryItem"], max_read_id: Optional[int] = None) -> None:
        self.peer = peer
        self.stories = stories
        self.max_read_id = max_read_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerStories":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        max_read_id = Int.read(b) if flags & (1 << 0) else None
        stories = TLObject.read(b)
        
        return PeerStories(peer=peer, stories=stories, max_read_id=max_read_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.max_read_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.max_read_id is not None:
            b.write(Int(self.max_read_id))
        
        b.write(Vector(self.stories))
        
        return b.getvalue()

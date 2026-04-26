
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class WebPageAttributeStory(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.WebPageAttribute`.

    Details:
        - Layer: ``224``
        - ID: ``2E94C3E7``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        id (``int`` ``32-bit``):
            N/A

        story (:obj:`StoryItem <pyrogram.raw.base.StoryItem>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "id", "story"]

    ID = 0x2e94c3e7
    QUALNAME = "types.WebPageAttributeStory"

    def __init__(self, *, peer: "raw.base.Peer", id: int, story: "raw.base.StoryItem" = None) -> None:
        self.peer = peer
        self.id = id
        self.story = story

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageAttributeStory":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        story = TLObject.read(b) if flags & (1 << 0) else None
        
        return WebPageAttributeStory(peer=peer, id=id, story=story)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.story is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        if self.story is not None:
            b.write(self.story.write())
        
        return b.getvalue()

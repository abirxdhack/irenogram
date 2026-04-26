
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateNewStoryReaction(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``1824E40B``

    Parameters:
        story_id (``int`` ``32-bit``):
            N/A

        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        reaction (:obj:`Reaction <pyrogram.raw.base.Reaction>`):
            N/A

    """

    __slots__: List[str] = ["story_id", "peer", "reaction"]

    ID = 0x1824e40b
    QUALNAME = "types.UpdateNewStoryReaction"

    def __init__(self, *, story_id: int, peer: "raw.base.Peer", reaction: "raw.base.Reaction") -> None:
        self.story_id = story_id
        self.peer = peer
        self.reaction = reaction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateNewStoryReaction":
        
        story_id = Int.read(b)
        
        peer = TLObject.read(b)
        
        reaction = TLObject.read(b)
        
        return UpdateNewStoryReaction(story_id=story_id, peer=peer, reaction=reaction)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.story_id))
        
        b.write(self.peer.write())
        
        b.write(self.reaction.write())
        
        return b.getvalue()

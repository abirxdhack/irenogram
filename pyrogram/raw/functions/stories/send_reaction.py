
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SendReaction(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``7FD736B2``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        story_id (``int`` ``32-bit``):
            N/A

        reaction (:obj:`Reaction <pyrogram.raw.base.Reaction>`):
            N/A

        add_to_recent (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "story_id", "reaction", "add_to_recent"]

    ID = 0x7fd736b2
    QUALNAME = "functions.stories.SendReaction"

    def __init__(self, *, peer: "raw.base.InputPeer", story_id: int, reaction: "raw.base.Reaction", add_to_recent: Optional[bool] = None) -> None:
        self.peer = peer
        self.story_id = story_id
        self.reaction = reaction
        self.add_to_recent = add_to_recent

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendReaction":
        
        flags = Int.read(b)
        
        add_to_recent = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        story_id = Int.read(b)
        
        reaction = TLObject.read(b)
        
        return SendReaction(peer=peer, story_id=story_id, reaction=reaction, add_to_recent=add_to_recent)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.add_to_recent else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.story_id))
        
        b.write(self.reaction.write())
        
        return b.getvalue()

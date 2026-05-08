
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StoryReaction(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StoryReaction`.

    Details:
        - Layer: ``224``
        - ID: ``6090D6D5``

    Parameters:
        peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        date (``int`` ``32-bit``):
            N/A

        reaction (:obj:`Reaction <pyrogram.raw.base.Reaction>`):
            N/A

    """

    __slots__: List[str] = ["peer_id", "date", "reaction"]

    ID = 0x6090d6d5
    QUALNAME = "types.StoryReaction"

    def __init__(self, *, peer_id: "raw.base.Peer", date: int, reaction: "raw.base.Reaction") -> None:
        self.peer_id = peer_id
        self.date = date
        self.reaction = reaction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryReaction":
        
        peer_id = TLObject.read(b)
        
        date = Int.read(b)
        
        reaction = TLObject.read(b)
        
        return StoryReaction(peer_id=peer_id, date=date, reaction=reaction)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer_id.write())
        
        b.write(Int(self.date))
        
        b.write(self.reaction.write())
        
        return b.getvalue()

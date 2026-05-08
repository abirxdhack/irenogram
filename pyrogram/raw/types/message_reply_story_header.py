
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageReplyStoryHeader(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageReplyHeader`.

    Details:
        - Layer: ``224``
        - ID: ``E5AF939``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        story_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["peer", "story_id"]

    ID = 0xe5af939
    QUALNAME = "types.MessageReplyStoryHeader"

    def __init__(self, *, peer: "raw.base.Peer", story_id: int) -> None:
        self.peer = peer
        self.story_id = story_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageReplyStoryHeader":
        
        peer = TLObject.read(b)
        
        story_id = Int.read(b)
        
        return MessageReplyStoryHeader(peer=peer, story_id=story_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.story_id))
        
        return b.getvalue()

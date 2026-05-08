
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PostInteractionCountersMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PostInteractionCounters`.

    Details:
        - Layer: ``224``
        - ID: ``E7058E7F``

    Parameters:
        msg_id (``int`` ``32-bit``):
            N/A

        views (``int`` ``32-bit``):
            N/A

        forwards (``int`` ``32-bit``):
            N/A

        reactions (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["msg_id", "views", "forwards", "reactions"]

    ID = 0xe7058e7f
    QUALNAME = "types.PostInteractionCountersMessage"

    def __init__(self, *, msg_id: int, views: int, forwards: int, reactions: int) -> None:
        self.msg_id = msg_id
        self.views = views
        self.forwards = forwards
        self.reactions = reactions

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PostInteractionCountersMessage":
        
        msg_id = Int.read(b)
        
        views = Int.read(b)
        
        forwards = Int.read(b)
        
        reactions = Int.read(b)
        
        return PostInteractionCountersMessage(msg_id=msg_id, views=views, forwards=forwards, reactions=reactions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.msg_id))
        
        b.write(Int(self.views))
        
        b.write(Int(self.forwards))
        
        b.write(Int(self.reactions))
        
        return b.getvalue()

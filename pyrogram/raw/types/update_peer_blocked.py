
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdatePeerBlocked(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``EBE07752``

    Parameters:
        peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        blocked (``bool``, *optional*):
            N/A

        blocked_my_stories_from (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer_id", "blocked", "blocked_my_stories_from"]

    ID = 0xebe07752
    QUALNAME = "types.UpdatePeerBlocked"

    def __init__(self, *, peer_id: "raw.base.Peer", blocked: Optional[bool] = None, blocked_my_stories_from: Optional[bool] = None) -> None:
        self.peer_id = peer_id
        self.blocked = blocked
        self.blocked_my_stories_from = blocked_my_stories_from

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePeerBlocked":
        
        flags = Int.read(b)
        
        blocked = True if flags & (1 << 0) else False
        blocked_my_stories_from = True if flags & (1 << 1) else False
        peer_id = TLObject.read(b)
        
        return UpdatePeerBlocked(peer_id=peer_id, blocked=blocked, blocked_my_stories_from=blocked_my_stories_from)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.blocked else 0
        flags |= (1 << 1) if self.blocked_my_stories_from else 0
        b.write(Int(flags))
        
        b.write(self.peer_id.write())
        
        return b.getvalue()

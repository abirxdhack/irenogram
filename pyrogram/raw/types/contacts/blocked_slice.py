
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BlockedSlice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.contacts.Blocked`.

    Details:
        - Layer: ``224``
        - ID: ``E1664194``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        blocked (List of :obj:`PeerBlocked <pyrogram.raw.base.PeerBlocked>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetBlocked
    """

    __slots__: List[str] = ["count", "blocked", "chats", "users"]

    ID = 0xe1664194
    QUALNAME = "types.contacts.BlockedSlice"

    def __init__(self, *, count: int, blocked: List["raw.base.PeerBlocked"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.count = count
        self.blocked = blocked
        self.chats = chats
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BlockedSlice":
        
        count = Int.read(b)
        
        blocked = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return BlockedSlice(count=count, blocked=blocked, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.count))
        
        b.write(Vector(self.blocked))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()

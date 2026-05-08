
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class VotesList(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.VotesList`.

    Details:
        - Layer: ``224``
        - ID: ``4899484E``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        votes (List of :obj:`MessagePeerVote <pyrogram.raw.base.MessagePeerVote>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        next_offset (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetPollVotes
    """

    __slots__: List[str] = ["count", "votes", "chats", "users", "next_offset"]

    ID = 0x4899484e
    QUALNAME = "types.messages.VotesList"

    def __init__(self, *, count: int, votes: List["raw.base.MessagePeerVote"], chats: List["raw.base.Chat"], users: List["raw.base.User"], next_offset: Optional[str] = None) -> None:
        self.count = count
        self.votes = votes
        self.chats = chats
        self.users = users
        self.next_offset = next_offset

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "VotesList":
        
        flags = Int.read(b)
        
        count = Int.read(b)
        
        votes = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        next_offset = String.read(b) if flags & (1 << 0) else None
        return VotesList(count=count, votes=votes, chats=chats, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Vector(self.votes))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        if self.next_offset is not None:
            b.write(String(self.next_offset))
        
        return b.getvalue()

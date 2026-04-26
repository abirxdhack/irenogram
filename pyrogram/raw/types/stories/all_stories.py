
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AllStories(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.stories.AllStories`.

    Details:
        - Layer: ``224``
        - ID: ``6EFC5E81``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        state (``str``):
            N/A

        peer_stories (List of :obj:`PeerStories <pyrogram.raw.base.PeerStories>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        stealth_mode (:obj:`StoriesStealthMode <pyrogram.raw.base.StoriesStealthMode>`):
            N/A

        has_more (``bool``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.GetAllStories
    """

    __slots__: List[str] = ["count", "state", "peer_stories", "chats", "users", "stealth_mode", "has_more"]

    ID = 0x6efc5e81
    QUALNAME = "types.stories.AllStories"

    def __init__(self, *, count: int, state: str, peer_stories: List["raw.base.PeerStories"], chats: List["raw.base.Chat"], users: List["raw.base.User"], stealth_mode: "raw.base.StoriesStealthMode", has_more: Optional[bool] = None) -> None:
        self.count = count
        self.state = state
        self.peer_stories = peer_stories
        self.chats = chats
        self.users = users
        self.stealth_mode = stealth_mode
        self.has_more = has_more

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AllStories":
        
        flags = Int.read(b)
        
        has_more = True if flags & (1 << 0) else False
        count = Int.read(b)
        
        state = String.read(b)
        
        peer_stories = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        stealth_mode = TLObject.read(b)
        
        return AllStories(count=count, state=state, peer_stories=peer_stories, chats=chats, users=users, stealth_mode=stealth_mode, has_more=has_more)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.has_more else 0
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(String(self.state))
        
        b.write(Vector(self.peer_stories))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        b.write(self.stealth_mode.write())
        
        return b.getvalue()

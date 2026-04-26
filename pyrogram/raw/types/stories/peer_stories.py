
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PeerStories(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.stories.PeerStories`.

    Details:
        - Layer: ``224``
        - ID: ``CAE68768``

    Parameters:
        stories (:obj:`PeerStories <pyrogram.raw.base.PeerStories>`):
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

            stories.GetPeerStories
    """

    __slots__: List[str] = ["stories", "chats", "users"]

    ID = 0xcae68768
    QUALNAME = "types.stories.PeerStories"

    def __init__(self, *, stories: "raw.base.PeerStories", chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.stories = stories
        self.chats = chats
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerStories":
        
        stories = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return PeerStories(stories=stories, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.stories.write())
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()

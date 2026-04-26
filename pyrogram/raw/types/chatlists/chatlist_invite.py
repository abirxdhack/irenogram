
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChatlistInvite(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.chatlists.ChatlistInvite`.

    Details:
        - Layer: ``224``
        - ID: ``F10ECE2F``

    Parameters:
        title (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

        peers (List of :obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        title_noanimate (``bool``, *optional*):
            N/A

        emoticon (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            chatlists.CheckChatlistInvite
    """

    __slots__: List[str] = ["title", "peers", "chats", "users", "title_noanimate", "emoticon"]

    ID = 0xf10ece2f
    QUALNAME = "types.chatlists.ChatlistInvite"

    def __init__(self, *, title: "raw.base.TextWithEntities", peers: List["raw.base.Peer"], chats: List["raw.base.Chat"], users: List["raw.base.User"], title_noanimate: Optional[bool] = None, emoticon: Optional[str] = None) -> None:
        self.title = title
        self.peers = peers
        self.chats = chats
        self.users = users
        self.title_noanimate = title_noanimate
        self.emoticon = emoticon

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatlistInvite":
        
        flags = Int.read(b)
        
        title_noanimate = True if flags & (1 << 1) else False
        title = TLObject.read(b)
        
        emoticon = String.read(b) if flags & (1 << 0) else None
        peers = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ChatlistInvite(title=title, peers=peers, chats=chats, users=users, title_noanimate=title_noanimate, emoticon=emoticon)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.title_noanimate else 0
        flags |= (1 << 0) if self.emoticon is not None else 0
        b.write(Int(flags))
        
        b.write(self.title.write())
        
        if self.emoticon is not None:
            b.write(String(self.emoticon))
        
        b.write(Vector(self.peers))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class QuickReplies(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.QuickReplies`.

    Details:
        - Layer: ``224``
        - ID: ``C68D6695``

    Parameters:
        quick_replies (List of :obj:`QuickReply <pyrogram.raw.base.QuickReply>`):
            N/A

        messages (List of :obj:`Message <pyrogram.raw.base.Message>`):
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

            messages.GetQuickReplies
    """

    __slots__: List[str] = ["quick_replies", "messages", "chats", "users"]

    ID = 0xc68d6695
    QUALNAME = "types.messages.QuickReplies"

    def __init__(self, *, quick_replies: List["raw.base.QuickReply"], messages: List["raw.base.Message"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.quick_replies = quick_replies
        self.messages = messages
        self.chats = chats
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "QuickReplies":
        
        quick_replies = TLObject.read(b)
        
        messages = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return QuickReplies(quick_replies=quick_replies, messages=messages, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.quick_replies))
        
        b.write(Vector(self.messages))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()

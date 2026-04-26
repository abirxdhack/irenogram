
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelMessages(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.Messages`.

    Details:
        - Layer: ``224``
        - ID: ``C776BA4E``

    Parameters:
        pts (``int`` ``32-bit``):
            N/A

        count (``int`` ``32-bit``):
            N/A

        messages (List of :obj:`Message <pyrogram.raw.base.Message>`):
            N/A

        topics (List of :obj:`ForumTopic <pyrogram.raw.base.ForumTopic>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        inexact (``bool``, *optional*):
            N/A

        offset_id_offset (``int`` ``32-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 16 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetMessages
            messages.GetHistory
            messages.Search
            messages.SearchGlobal
            messages.GetUnreadMentions
            messages.GetRecentLocations
            messages.GetScheduledHistory
            messages.GetScheduledMessages
            messages.GetReplies
            messages.GetUnreadReactions
            messages.SearchSentMedia
            messages.GetSavedHistory
            messages.GetQuickReplyMessages
            messages.GetUnreadPollVotes
            channels.GetMessages
            channels.SearchPosts
    """

    __slots__: List[str] = ["pts", "count", "messages", "topics", "chats", "users", "inexact", "offset_id_offset"]

    ID = 0xc776ba4e
    QUALNAME = "types.messages.ChannelMessages"

    def __init__(self, *, pts: int, count: int, messages: List["raw.base.Message"], topics: List["raw.base.ForumTopic"], chats: List["raw.base.Chat"], users: List["raw.base.User"], inexact: Optional[bool] = None, offset_id_offset: Optional[int] = None) -> None:
        self.pts = pts
        self.count = count
        self.messages = messages
        self.topics = topics
        self.chats = chats
        self.users = users
        self.inexact = inexact
        self.offset_id_offset = offset_id_offset

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelMessages":
        
        flags = Int.read(b)
        
        inexact = True if flags & (1 << 1) else False
        pts = Int.read(b)
        
        count = Int.read(b)
        
        offset_id_offset = Int.read(b) if flags & (1 << 2) else None
        messages = TLObject.read(b)
        
        topics = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ChannelMessages(pts=pts, count=count, messages=messages, topics=topics, chats=chats, users=users, inexact=inexact, offset_id_offset=offset_id_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.inexact else 0
        flags |= (1 << 2) if self.offset_id_offset is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.pts))
        
        b.write(Int(self.count))
        
        if self.offset_id_offset is not None:
            b.write(Int(self.offset_id_offset))
        
        b.write(Vector(self.messages))
        
        b.write(Vector(self.topics))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()

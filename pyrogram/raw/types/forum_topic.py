
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ForumTopic(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ForumTopic`.

    Details:
        - Layer: ``224``
        - ID: ``FCDAD815``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        title (``str``):
            N/A

        icon_color (``int`` ``32-bit``):
            N/A

        top_message (``int`` ``32-bit``):
            N/A

        read_inbox_max_id (``int`` ``32-bit``):
            N/A

        read_outbox_max_id (``int`` ``32-bit``):
            N/A

        unread_count (``int`` ``32-bit``):
            N/A

        unread_mentions_count (``int`` ``32-bit``):
            N/A

        unread_reactions_count (``int`` ``32-bit``):
            N/A

        unread_poll_votes_count (``int`` ``32-bit``):
            N/A

        from_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        notify_settings (:obj:`PeerNotifySettings <pyrogram.raw.base.PeerNotifySettings>`):
            N/A

        my (``bool``, *optional*):
            N/A

        closed (``bool``, *optional*):
            N/A

        pinned (``bool``, *optional*):
            N/A

        short (``bool``, *optional*):
            N/A

        hidden (``bool``, *optional*):
            N/A

        title_missing (``bool``, *optional*):
            N/A

        icon_emoji_id (``int`` ``64-bit``, *optional*):
            N/A

        draft (:obj:`DraftMessage <pyrogram.raw.base.DraftMessage>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "date", "peer", "title", "icon_color", "top_message", "read_inbox_max_id", "read_outbox_max_id", "unread_count", "unread_mentions_count", "unread_reactions_count", "unread_poll_votes_count", "from_id", "notify_settings", "my", "closed", "pinned", "short", "hidden", "title_missing", "icon_emoji_id", "draft"]

    ID = 0xfcdad815
    QUALNAME = "types.ForumTopic"

    def __init__(self, *, id: int, date: int, peer: "raw.base.Peer", title: str, icon_color: int, top_message: int, read_inbox_max_id: int, read_outbox_max_id: int, unread_count: int, unread_mentions_count: int, unread_reactions_count: int, unread_poll_votes_count: int, from_id: "raw.base.Peer", notify_settings: "raw.base.PeerNotifySettings", my: Optional[bool] = None, closed: Optional[bool] = None, pinned: Optional[bool] = None, short: Optional[bool] = None, hidden: Optional[bool] = None, title_missing: Optional[bool] = None, icon_emoji_id: Optional[int] = None, draft: "raw.base.DraftMessage" = None) -> None:
        self.id = id
        self.date = date
        self.peer = peer
        self.title = title
        self.icon_color = icon_color
        self.top_message = top_message
        self.read_inbox_max_id = read_inbox_max_id
        self.read_outbox_max_id = read_outbox_max_id
        self.unread_count = unread_count
        self.unread_mentions_count = unread_mentions_count
        self.unread_reactions_count = unread_reactions_count
        self.unread_poll_votes_count = unread_poll_votes_count
        self.from_id = from_id
        self.notify_settings = notify_settings
        self.my = my
        self.closed = closed
        self.pinned = pinned
        self.short = short
        self.hidden = hidden
        self.title_missing = title_missing
        self.icon_emoji_id = icon_emoji_id
        self.draft = draft

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ForumTopic":
        
        flags = Int.read(b)
        
        my = True if flags & (1 << 1) else False
        closed = True if flags & (1 << 2) else False
        pinned = True if flags & (1 << 3) else False
        short = True if flags & (1 << 5) else False
        hidden = True if flags & (1 << 6) else False
        title_missing = True if flags & (1 << 7) else False
        id = Int.read(b)
        
        date = Int.read(b)
        
        peer = TLObject.read(b)
        
        title = String.read(b)
        
        icon_color = Int.read(b)
        
        icon_emoji_id = Long.read(b) if flags & (1 << 0) else None
        top_message = Int.read(b)
        
        read_inbox_max_id = Int.read(b)
        
        read_outbox_max_id = Int.read(b)
        
        unread_count = Int.read(b)
        
        unread_mentions_count = Int.read(b)
        
        unread_reactions_count = Int.read(b)
        
        unread_poll_votes_count = Int.read(b)
        
        from_id = TLObject.read(b)
        
        notify_settings = TLObject.read(b)
        
        draft = TLObject.read(b) if flags & (1 << 4) else None
        
        return ForumTopic(id=id, date=date, peer=peer, title=title, icon_color=icon_color, top_message=top_message, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id, unread_count=unread_count, unread_mentions_count=unread_mentions_count, unread_reactions_count=unread_reactions_count, unread_poll_votes_count=unread_poll_votes_count, from_id=from_id, notify_settings=notify_settings, my=my, closed=closed, pinned=pinned, short=short, hidden=hidden, title_missing=title_missing, icon_emoji_id=icon_emoji_id, draft=draft)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.my else 0
        flags |= (1 << 2) if self.closed else 0
        flags |= (1 << 3) if self.pinned else 0
        flags |= (1 << 5) if self.short else 0
        flags |= (1 << 6) if self.hidden else 0
        flags |= (1 << 7) if self.title_missing else 0
        flags |= (1 << 0) if self.icon_emoji_id is not None else 0
        flags |= (1 << 4) if self.draft is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(Int(self.date))
        
        b.write(self.peer.write())
        
        b.write(String(self.title))
        
        b.write(Int(self.icon_color))
        
        if self.icon_emoji_id is not None:
            b.write(Long(self.icon_emoji_id))
        
        b.write(Int(self.top_message))
        
        b.write(Int(self.read_inbox_max_id))
        
        b.write(Int(self.read_outbox_max_id))
        
        b.write(Int(self.unread_count))
        
        b.write(Int(self.unread_mentions_count))
        
        b.write(Int(self.unread_reactions_count))
        
        b.write(Int(self.unread_poll_votes_count))
        
        b.write(self.from_id.write())
        
        b.write(self.notify_settings.write())
        
        if self.draft is not None:
            b.write(self.draft.write())
        
        return b.getvalue()

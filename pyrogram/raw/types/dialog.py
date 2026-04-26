
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class Dialog(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Dialog`.

    Details:
        - Layer: ``224``
        - ID: ``FC89F7F3``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
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

        notify_settings (:obj:`PeerNotifySettings <pyrogram.raw.base.PeerNotifySettings>`):
            N/A

        pinned (``bool``, *optional*):
            N/A

        unread_mark (``bool``, *optional*):
            N/A

        view_forum_as_messages (``bool``, *optional*):
            N/A

        pts (``int`` ``32-bit``, *optional*):
            N/A

        draft (:obj:`DraftMessage <pyrogram.raw.base.DraftMessage>`, *optional*):
            N/A

        folder_id (``int`` ``32-bit``, *optional*):
            N/A

        ttl_period (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "top_message", "read_inbox_max_id", "read_outbox_max_id", "unread_count", "unread_mentions_count", "unread_reactions_count", "unread_poll_votes_count", "notify_settings", "pinned", "unread_mark", "view_forum_as_messages", "pts", "draft", "folder_id", "ttl_period"]

    ID = 0xfc89f7f3
    QUALNAME = "types.Dialog"

    def __init__(self, *, peer: "raw.base.Peer", top_message: int, read_inbox_max_id: int, read_outbox_max_id: int, unread_count: int, unread_mentions_count: int, unread_reactions_count: int, unread_poll_votes_count: int, notify_settings: "raw.base.PeerNotifySettings", pinned: Optional[bool] = None, unread_mark: Optional[bool] = None, view_forum_as_messages: Optional[bool] = None, pts: Optional[int] = None, draft: "raw.base.DraftMessage" = None, folder_id: Optional[int] = None, ttl_period: Optional[int] = None) -> None:
        self.peer = peer
        self.top_message = top_message
        self.read_inbox_max_id = read_inbox_max_id
        self.read_outbox_max_id = read_outbox_max_id
        self.unread_count = unread_count
        self.unread_mentions_count = unread_mentions_count
        self.unread_reactions_count = unread_reactions_count
        self.unread_poll_votes_count = unread_poll_votes_count
        self.notify_settings = notify_settings
        self.pinned = pinned
        self.unread_mark = unread_mark
        self.view_forum_as_messages = view_forum_as_messages
        self.pts = pts
        self.draft = draft
        self.folder_id = folder_id
        self.ttl_period = ttl_period

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Dialog":
        
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 2) else False
        unread_mark = True if flags & (1 << 3) else False
        view_forum_as_messages = True if flags & (1 << 6) else False
        peer = TLObject.read(b)
        
        top_message = Int.read(b)
        
        read_inbox_max_id = Int.read(b)
        
        read_outbox_max_id = Int.read(b)
        
        unread_count = Int.read(b)
        
        unread_mentions_count = Int.read(b)
        
        unread_reactions_count = Int.read(b)
        
        unread_poll_votes_count = Int.read(b)
        
        notify_settings = TLObject.read(b)
        
        pts = Int.read(b) if flags & (1 << 0) else None
        draft = TLObject.read(b) if flags & (1 << 1) else None
        
        folder_id = Int.read(b) if flags & (1 << 4) else None
        ttl_period = Int.read(b) if flags & (1 << 5) else None
        return Dialog(peer=peer, top_message=top_message, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id, unread_count=unread_count, unread_mentions_count=unread_mentions_count, unread_reactions_count=unread_reactions_count, unread_poll_votes_count=unread_poll_votes_count, notify_settings=notify_settings, pinned=pinned, unread_mark=unread_mark, view_forum_as_messages=view_forum_as_messages, pts=pts, draft=draft, folder_id=folder_id, ttl_period=ttl_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.pinned else 0
        flags |= (1 << 3) if self.unread_mark else 0
        flags |= (1 << 6) if self.view_forum_as_messages else 0
        flags |= (1 << 0) if self.pts is not None else 0
        flags |= (1 << 1) if self.draft is not None else 0
        flags |= (1 << 4) if self.folder_id is not None else 0
        flags |= (1 << 5) if self.ttl_period is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.top_message))
        
        b.write(Int(self.read_inbox_max_id))
        
        b.write(Int(self.read_outbox_max_id))
        
        b.write(Int(self.unread_count))
        
        b.write(Int(self.unread_mentions_count))
        
        b.write(Int(self.unread_reactions_count))
        
        b.write(Int(self.unread_poll_votes_count))
        
        b.write(self.notify_settings.write())
        
        if self.pts is not None:
            b.write(Int(self.pts))
        
        if self.draft is not None:
            b.write(self.draft.write())
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        return b.getvalue()

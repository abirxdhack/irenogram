
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageService(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Message`.

    Details:
        - Layer: ``224``
        - ID: ``7A800E0A``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        date (``int`` ``32-bit``):
            N/A

        action (:obj:`MessageAction <pyrogram.raw.base.MessageAction>`):
            N/A

        out (``bool``, *optional*):
            N/A

        mentioned (``bool``, *optional*):
            N/A

        media_unread (``bool``, *optional*):
            N/A

        reactions_are_possible (``bool``, *optional*):
            N/A

        silent (``bool``, *optional*):
            N/A

        post (``bool``, *optional*):
            N/A

        legacy (``bool``, *optional*):
            N/A

        from_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        saved_peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        reply_to (:obj:`MessageReplyHeader <pyrogram.raw.base.MessageReplyHeader>`, *optional*):
            N/A

        reactions (:obj:`MessageReactions <pyrogram.raw.base.MessageReactions>`, *optional*):
            N/A

        ttl_period (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "peer_id", "date", "action", "out", "mentioned", "media_unread", "reactions_are_possible", "silent", "post", "legacy", "from_id", "saved_peer_id", "reply_to", "reactions", "ttl_period"]

    ID = 0x7a800e0a
    QUALNAME = "types.MessageService"

    def __init__(self, *, id: int, peer_id: "raw.base.Peer", date: int, action: "raw.base.MessageAction", out: Optional[bool] = None, mentioned: Optional[bool] = None, media_unread: Optional[bool] = None, reactions_are_possible: Optional[bool] = None, silent: Optional[bool] = None, post: Optional[bool] = None, legacy: Optional[bool] = None, from_id: "raw.base.Peer" = None, saved_peer_id: "raw.base.Peer" = None, reply_to: "raw.base.MessageReplyHeader" = None, reactions: "raw.base.MessageReactions" = None, ttl_period: Optional[int] = None) -> None:
        self.id = id
        self.peer_id = peer_id
        self.date = date
        self.action = action
        self.out = out
        self.mentioned = mentioned
        self.media_unread = media_unread
        self.reactions_are_possible = reactions_are_possible
        self.silent = silent
        self.post = post
        self.legacy = legacy
        self.from_id = from_id
        self.saved_peer_id = saved_peer_id
        self.reply_to = reply_to
        self.reactions = reactions
        self.ttl_period = ttl_period

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageService":
        
        flags = Int.read(b)
        
        out = True if flags & (1 << 1) else False
        mentioned = True if flags & (1 << 4) else False
        media_unread = True if flags & (1 << 5) else False
        reactions_are_possible = True if flags & (1 << 9) else False
        silent = True if flags & (1 << 13) else False
        post = True if flags & (1 << 14) else False
        legacy = True if flags & (1 << 19) else False
        id = Int.read(b)
        
        from_id = TLObject.read(b) if flags & (1 << 8) else None
        
        peer_id = TLObject.read(b)
        
        saved_peer_id = TLObject.read(b) if flags & (1 << 28) else None
        
        reply_to = TLObject.read(b) if flags & (1 << 3) else None
        
        date = Int.read(b)
        
        action = TLObject.read(b)
        
        reactions = TLObject.read(b) if flags & (1 << 20) else None
        
        ttl_period = Int.read(b) if flags & (1 << 25) else None
        return MessageService(id=id, peer_id=peer_id, date=date, action=action, out=out, mentioned=mentioned, media_unread=media_unread, reactions_are_possible=reactions_are_possible, silent=silent, post=post, legacy=legacy, from_id=from_id, saved_peer_id=saved_peer_id, reply_to=reply_to, reactions=reactions, ttl_period=ttl_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.out else 0
        flags |= (1 << 4) if self.mentioned else 0
        flags |= (1 << 5) if self.media_unread else 0
        flags |= (1 << 9) if self.reactions_are_possible else 0
        flags |= (1 << 13) if self.silent else 0
        flags |= (1 << 14) if self.post else 0
        flags |= (1 << 19) if self.legacy else 0
        flags |= (1 << 8) if self.from_id is not None else 0
        flags |= (1 << 28) if self.saved_peer_id is not None else 0
        flags |= (1 << 3) if self.reply_to is not None else 0
        flags |= (1 << 20) if self.reactions is not None else 0
        flags |= (1 << 25) if self.ttl_period is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        if self.from_id is not None:
            b.write(self.from_id.write())
        
        b.write(self.peer_id.write())
        
        if self.saved_peer_id is not None:
            b.write(self.saved_peer_id.write())
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        b.write(Int(self.date))
        
        b.write(self.action.write())
        
        if self.reactions is not None:
            b.write(self.reactions.write())
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        return b.getvalue()

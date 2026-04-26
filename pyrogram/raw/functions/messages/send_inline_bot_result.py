
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SendInlineBotResult(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``C0CF7646``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        random_id (``int`` ``64-bit``):
            N/A

        query_id (``int`` ``64-bit``):
            N/A

        id (``str``):
            N/A

        silent (``bool``, *optional*):
            N/A

        background (``bool``, *optional*):
            N/A

        clear_draft (``bool``, *optional*):
            N/A

        hide_via (``bool``, *optional*):
            N/A

        reply_to (:obj:`InputReplyTo <pyrogram.raw.base.InputReplyTo>`, *optional*):
            N/A

        schedule_date (``int`` ``32-bit``, *optional*):
            N/A

        send_as (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

        quick_reply_shortcut (:obj:`InputQuickReplyShortcut <pyrogram.raw.base.InputQuickReplyShortcut>`, *optional*):
            N/A

        allow_paid_stars (``int`` ``64-bit``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "random_id", "query_id", "id", "silent", "background", "clear_draft", "hide_via", "reply_to", "schedule_date", "send_as", "quick_reply_shortcut", "allow_paid_stars"]

    ID = 0xc0cf7646
    QUALNAME = "functions.messages.SendInlineBotResult"

    def __init__(self, *, peer: "raw.base.InputPeer", random_id: int, query_id: int, id: str, silent: Optional[bool] = None, background: Optional[bool] = None, clear_draft: Optional[bool] = None, hide_via: Optional[bool] = None, reply_to: "raw.base.InputReplyTo" = None, schedule_date: Optional[int] = None, send_as: "raw.base.InputPeer" = None, quick_reply_shortcut: "raw.base.InputQuickReplyShortcut" = None, allow_paid_stars: Optional[int] = None) -> None:
        self.peer = peer
        self.random_id = random_id
        self.query_id = query_id
        self.id = id
        self.silent = silent
        self.background = background
        self.clear_draft = clear_draft
        self.hide_via = hide_via
        self.reply_to = reply_to
        self.schedule_date = schedule_date
        self.send_as = send_as
        self.quick_reply_shortcut = quick_reply_shortcut
        self.allow_paid_stars = allow_paid_stars

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendInlineBotResult":
        
        flags = Int.read(b)
        
        silent = True if flags & (1 << 5) else False
        background = True if flags & (1 << 6) else False
        clear_draft = True if flags & (1 << 7) else False
        hide_via = True if flags & (1 << 11) else False
        peer = TLObject.read(b)
        
        reply_to = TLObject.read(b) if flags & (1 << 0) else None
        
        random_id = Long.read(b)
        
        query_id = Long.read(b)
        
        id = String.read(b)
        
        schedule_date = Int.read(b) if flags & (1 << 10) else None
        send_as = TLObject.read(b) if flags & (1 << 13) else None
        
        quick_reply_shortcut = TLObject.read(b) if flags & (1 << 17) else None
        
        allow_paid_stars = Long.read(b) if flags & (1 << 21) else None
        return SendInlineBotResult(peer=peer, random_id=random_id, query_id=query_id, id=id, silent=silent, background=background, clear_draft=clear_draft, hide_via=hide_via, reply_to=reply_to, schedule_date=schedule_date, send_as=send_as, quick_reply_shortcut=quick_reply_shortcut, allow_paid_stars=allow_paid_stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.silent else 0
        flags |= (1 << 6) if self.background else 0
        flags |= (1 << 7) if self.clear_draft else 0
        flags |= (1 << 11) if self.hide_via else 0
        flags |= (1 << 0) if self.reply_to is not None else 0
        flags |= (1 << 10) if self.schedule_date is not None else 0
        flags |= (1 << 13) if self.send_as is not None else 0
        flags |= (1 << 17) if self.quick_reply_shortcut is not None else 0
        flags |= (1 << 21) if self.allow_paid_stars is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        b.write(Long(self.random_id))
        
        b.write(Long(self.query_id))
        
        b.write(String(self.id))
        
        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))
        
        if self.send_as is not None:
            b.write(self.send_as.write())
        
        if self.quick_reply_shortcut is not None:
            b.write(self.quick_reply_shortcut.write())
        
        if self.allow_paid_stars is not None:
            b.write(Long(self.allow_paid_stars))
        
        return b.getvalue()

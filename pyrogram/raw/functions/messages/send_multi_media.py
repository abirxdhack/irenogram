
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SendMultiMedia(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``1BF89D74``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        multi_media (List of :obj:`InputSingleMedia <pyrogram.raw.base.InputSingleMedia>`):
            N/A

        silent (``bool``, *optional*):
            N/A

        background (``bool``, *optional*):
            N/A

        clear_draft (``bool``, *optional*):
            N/A

        noforwards (``bool``, *optional*):
            N/A

        update_stickersets_order (``bool``, *optional*):
            N/A

        invert_media (``bool``, *optional*):
            N/A

        allow_paid_floodskip (``bool``, *optional*):
            N/A

        reply_to (:obj:`InputReplyTo <pyrogram.raw.base.InputReplyTo>`, *optional*):
            N/A

        schedule_date (``int`` ``32-bit``, *optional*):
            N/A

        send_as (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

        quick_reply_shortcut (:obj:`InputQuickReplyShortcut <pyrogram.raw.base.InputQuickReplyShortcut>`, *optional*):
            N/A

        effect (``int`` ``64-bit``, *optional*):
            N/A

        allow_paid_stars (``int`` ``64-bit``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "multi_media", "silent", "background", "clear_draft", "noforwards", "update_stickersets_order", "invert_media", "allow_paid_floodskip", "reply_to", "schedule_date", "send_as", "quick_reply_shortcut", "effect", "allow_paid_stars"]

    ID = 0x1bf89d74
    QUALNAME = "functions.messages.SendMultiMedia"

    def __init__(self, *, peer: "raw.base.InputPeer", multi_media: List["raw.base.InputSingleMedia"], silent: Optional[bool] = None, background: Optional[bool] = None, clear_draft: Optional[bool] = None, noforwards: Optional[bool] = None, update_stickersets_order: Optional[bool] = None, invert_media: Optional[bool] = None, allow_paid_floodskip: Optional[bool] = None, reply_to: "raw.base.InputReplyTo" = None, schedule_date: Optional[int] = None, send_as: "raw.base.InputPeer" = None, quick_reply_shortcut: "raw.base.InputQuickReplyShortcut" = None, effect: Optional[int] = None, allow_paid_stars: Optional[int] = None) -> None:
        self.peer = peer
        self.multi_media = multi_media
        self.silent = silent
        self.background = background
        self.clear_draft = clear_draft
        self.noforwards = noforwards
        self.update_stickersets_order = update_stickersets_order
        self.invert_media = invert_media
        self.allow_paid_floodskip = allow_paid_floodskip
        self.reply_to = reply_to
        self.schedule_date = schedule_date
        self.send_as = send_as
        self.quick_reply_shortcut = quick_reply_shortcut
        self.effect = effect
        self.allow_paid_stars = allow_paid_stars

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendMultiMedia":
        
        flags = Int.read(b)
        
        silent = True if flags & (1 << 5) else False
        background = True if flags & (1 << 6) else False
        clear_draft = True if flags & (1 << 7) else False
        noforwards = True if flags & (1 << 14) else False
        update_stickersets_order = True if flags & (1 << 15) else False
        invert_media = True if flags & (1 << 16) else False
        allow_paid_floodskip = True if flags & (1 << 19) else False
        peer = TLObject.read(b)
        
        reply_to = TLObject.read(b) if flags & (1 << 0) else None
        
        multi_media = TLObject.read(b)
        
        schedule_date = Int.read(b) if flags & (1 << 10) else None
        send_as = TLObject.read(b) if flags & (1 << 13) else None
        
        quick_reply_shortcut = TLObject.read(b) if flags & (1 << 17) else None
        
        effect = Long.read(b) if flags & (1 << 18) else None
        allow_paid_stars = Long.read(b) if flags & (1 << 21) else None
        return SendMultiMedia(peer=peer, multi_media=multi_media, silent=silent, background=background, clear_draft=clear_draft, noforwards=noforwards, update_stickersets_order=update_stickersets_order, invert_media=invert_media, allow_paid_floodskip=allow_paid_floodskip, reply_to=reply_to, schedule_date=schedule_date, send_as=send_as, quick_reply_shortcut=quick_reply_shortcut, effect=effect, allow_paid_stars=allow_paid_stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.silent else 0
        flags |= (1 << 6) if self.background else 0
        flags |= (1 << 7) if self.clear_draft else 0
        flags |= (1 << 14) if self.noforwards else 0
        flags |= (1 << 15) if self.update_stickersets_order else 0
        flags |= (1 << 16) if self.invert_media else 0
        flags |= (1 << 19) if self.allow_paid_floodskip else 0
        flags |= (1 << 0) if self.reply_to is not None else 0
        flags |= (1 << 10) if self.schedule_date is not None else 0
        flags |= (1 << 13) if self.send_as is not None else 0
        flags |= (1 << 17) if self.quick_reply_shortcut is not None else 0
        flags |= (1 << 18) if self.effect is not None else 0
        flags |= (1 << 21) if self.allow_paid_stars is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        b.write(Vector(self.multi_media))
        
        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))
        
        if self.send_as is not None:
            b.write(self.send_as.write())
        
        if self.quick_reply_shortcut is not None:
            b.write(self.quick_reply_shortcut.write())
        
        if self.effect is not None:
            b.write(Long(self.effect))
        
        if self.allow_paid_stars is not None:
            b.write(Long(self.allow_paid_stars))
        
        return b.getvalue()

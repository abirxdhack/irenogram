
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DraftMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DraftMessage`.

    Details:
        - Layer: ``224``
        - ID: ``96EAA5EB``

    Parameters:
        message (``str``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        no_webpage (``bool``, *optional*):
            N/A

        invert_media (``bool``, *optional*):
            N/A

        reply_to (:obj:`InputReplyTo <pyrogram.raw.base.InputReplyTo>`, *optional*):
            N/A

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            N/A

        media (:obj:`InputMedia <pyrogram.raw.base.InputMedia>`, *optional*):
            N/A

        effect (``int`` ``64-bit``, *optional*):
            N/A

        suggested_post (:obj:`SuggestedPost <pyrogram.raw.base.SuggestedPost>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["message", "date", "no_webpage", "invert_media", "reply_to", "entities", "media", "effect", "suggested_post"]

    ID = 0x96eaa5eb
    QUALNAME = "types.DraftMessage"

    def __init__(self, *, message: str, date: int, no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, reply_to: "raw.base.InputReplyTo" = None, entities: Optional[List["raw.base.MessageEntity"]] = None, media: "raw.base.InputMedia" = None, effect: Optional[int] = None, suggested_post: "raw.base.SuggestedPost" = None) -> None:
        self.message = message
        self.date = date
        self.no_webpage = no_webpage
        self.invert_media = invert_media
        self.reply_to = reply_to
        self.entities = entities
        self.media = media
        self.effect = effect
        self.suggested_post = suggested_post

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DraftMessage":
        
        flags = Int.read(b)
        
        no_webpage = True if flags & (1 << 1) else False
        invert_media = True if flags & (1 << 6) else False
        reply_to = TLObject.read(b) if flags & (1 << 4) else None
        
        message = String.read(b)
        
        entities = TLObject.read(b) if flags & (1 << 3) else []
        
        media = TLObject.read(b) if flags & (1 << 5) else None
        
        date = Int.read(b)
        
        effect = Long.read(b) if flags & (1 << 7) else None
        suggested_post = TLObject.read(b) if flags & (1 << 8) else None
        
        return DraftMessage(message=message, date=date, no_webpage=no_webpage, invert_media=invert_media, reply_to=reply_to, entities=entities, media=media, effect=effect, suggested_post=suggested_post)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.no_webpage else 0
        flags |= (1 << 6) if self.invert_media else 0
        flags |= (1 << 4) if self.reply_to is not None else 0
        flags |= (1 << 3) if self.entities else 0
        flags |= (1 << 5) if self.media is not None else 0
        flags |= (1 << 7) if self.effect is not None else 0
        flags |= (1 << 8) if self.suggested_post is not None else 0
        b.write(Int(flags))
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        b.write(String(self.message))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.media is not None:
            b.write(self.media.write())
        
        b.write(Int(self.date))
        
        if self.effect is not None:
            b.write(Long(self.effect))
        
        if self.suggested_post is not None:
            b.write(self.suggested_post.write())
        
        return b.getvalue()

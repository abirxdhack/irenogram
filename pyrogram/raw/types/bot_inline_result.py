
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BotInlineResult(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotInlineResult`.

    Details:
        - Layer: ``224``
        - ID: ``11965F3A``

    Parameters:
        id (``str``):
            N/A

        type (``str``):
            N/A

        send_message (:obj:`BotInlineMessage <pyrogram.raw.base.BotInlineMessage>`):
            N/A

        title (``str``, *optional*):
            N/A

        description (``str``, *optional*):
            N/A

        url (``str``, *optional*):
            N/A

        thumb (:obj:`WebDocument <pyrogram.raw.base.WebDocument>`, *optional*):
            N/A

        content (:obj:`WebDocument <pyrogram.raw.base.WebDocument>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "type", "send_message", "title", "description", "url", "thumb", "content"]

    ID = 0x11965f3a
    QUALNAME = "types.BotInlineResult"

    def __init__(self, *, id: str, type: str, send_message: "raw.base.BotInlineMessage", title: Optional[str] = None, description: Optional[str] = None, url: Optional[str] = None, thumb: "raw.base.WebDocument" = None, content: "raw.base.WebDocument" = None) -> None:
        self.id = id
        self.type = type
        self.send_message = send_message
        self.title = title
        self.description = description
        self.url = url
        self.thumb = thumb
        self.content = content

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInlineResult":
        
        flags = Int.read(b)
        
        id = String.read(b)
        
        type = String.read(b)
        
        title = String.read(b) if flags & (1 << 1) else None
        description = String.read(b) if flags & (1 << 2) else None
        url = String.read(b) if flags & (1 << 3) else None
        thumb = TLObject.read(b) if flags & (1 << 4) else None
        
        content = TLObject.read(b) if flags & (1 << 5) else None
        
        send_message = TLObject.read(b)
        
        return BotInlineResult(id=id, type=type, send_message=send_message, title=title, description=description, url=url, thumb=thumb, content=content)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.title is not None else 0
        flags |= (1 << 2) if self.description is not None else 0
        flags |= (1 << 3) if self.url is not None else 0
        flags |= (1 << 4) if self.thumb is not None else 0
        flags |= (1 << 5) if self.content is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.id))
        
        b.write(String(self.type))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.description is not None:
            b.write(String(self.description))
        
        if self.url is not None:
            b.write(String(self.url))
        
        if self.thumb is not None:
            b.write(self.thumb.write())
        
        if self.content is not None:
            b.write(self.content.write())
        
        b.write(self.send_message.write())
        
        return b.getvalue()

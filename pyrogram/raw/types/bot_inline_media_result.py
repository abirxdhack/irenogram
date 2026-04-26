
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BotInlineMediaResult(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotInlineResult`.

    Details:
        - Layer: ``224``
        - ID: ``17DB940B``

    Parameters:
        id (``str``):
            N/A

        type (``str``):
            N/A

        send_message (:obj:`BotInlineMessage <pyrogram.raw.base.BotInlineMessage>`):
            N/A

        photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            N/A

        document (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

        title (``str``, *optional*):
            N/A

        description (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "type", "send_message", "photo", "document", "title", "description"]

    ID = 0x17db940b
    QUALNAME = "types.BotInlineMediaResult"

    def __init__(self, *, id: str, type: str, send_message: "raw.base.BotInlineMessage", photo: "raw.base.Photo" = None, document: "raw.base.Document" = None, title: Optional[str] = None, description: Optional[str] = None) -> None:
        self.id = id
        self.type = type
        self.send_message = send_message
        self.photo = photo
        self.document = document
        self.title = title
        self.description = description

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInlineMediaResult":
        
        flags = Int.read(b)
        
        id = String.read(b)
        
        type = String.read(b)
        
        photo = TLObject.read(b) if flags & (1 << 0) else None
        
        document = TLObject.read(b) if flags & (1 << 1) else None
        
        title = String.read(b) if flags & (1 << 2) else None
        description = String.read(b) if flags & (1 << 3) else None
        send_message = TLObject.read(b)
        
        return BotInlineMediaResult(id=id, type=type, send_message=send_message, photo=photo, document=document, title=title, description=description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.photo is not None else 0
        flags |= (1 << 1) if self.document is not None else 0
        flags |= (1 << 2) if self.title is not None else 0
        flags |= (1 << 3) if self.description is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.id))
        
        b.write(String(self.type))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.description is not None:
            b.write(String(self.description))
        
        b.write(self.send_message.write())
        
        return b.getvalue()

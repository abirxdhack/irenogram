
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputBotInlineResultDocument(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputBotInlineResult`.

    Details:
        - Layer: ``224``
        - ID: ``FFF8FDC4``

    Parameters:
        id (``str``):
            N/A

        type (``str``):
            N/A

        document (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            N/A

        send_message (:obj:`InputBotInlineMessage <pyrogram.raw.base.InputBotInlineMessage>`):
            N/A

        title (``str``, *optional*):
            N/A

        description (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "type", "document", "send_message", "title", "description"]

    ID = 0xfff8fdc4
    QUALNAME = "types.InputBotInlineResultDocument"

    def __init__(self, *, id: str, type: str, document: "raw.base.InputDocument", send_message: "raw.base.InputBotInlineMessage", title: Optional[str] = None, description: Optional[str] = None) -> None:
        self.id = id
        self.type = type
        self.document = document
        self.send_message = send_message
        self.title = title
        self.description = description

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotInlineResultDocument":
        
        flags = Int.read(b)
        
        id = String.read(b)
        
        type = String.read(b)
        
        title = String.read(b) if flags & (1 << 1) else None
        description = String.read(b) if flags & (1 << 2) else None
        document = TLObject.read(b)
        
        send_message = TLObject.read(b)
        
        return InputBotInlineResultDocument(id=id, type=type, document=document, send_message=send_message, title=title, description=description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.title is not None else 0
        flags |= (1 << 2) if self.description is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.id))
        
        b.write(String(self.type))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.description is not None:
            b.write(String(self.description))
        
        b.write(self.document.write())
        
        b.write(self.send_message.write())
        
        return b.getvalue()

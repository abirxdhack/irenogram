
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AppUpdate(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.AppUpdate`.

    Details:
        - Layer: ``224``
        - ID: ``CCBBCE30``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        version (``str``):
            N/A

        text (``str``):
            N/A

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`):
            N/A

        can_not_skip (``bool``, *optional*):
            N/A

        document (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

        url (``str``, *optional*):
            N/A

        sticker (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetAppUpdate
    """

    __slots__: List[str] = ["id", "version", "text", "entities", "can_not_skip", "document", "url", "sticker"]

    ID = 0xccbbce30
    QUALNAME = "types.help.AppUpdate"

    def __init__(self, *, id: int, version: str, text: str, entities: List["raw.base.MessageEntity"], can_not_skip: Optional[bool] = None, document: "raw.base.Document" = None, url: Optional[str] = None, sticker: "raw.base.Document" = None) -> None:
        self.id = id
        self.version = version
        self.text = text
        self.entities = entities
        self.can_not_skip = can_not_skip
        self.document = document
        self.url = url
        self.sticker = sticker

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AppUpdate":
        
        flags = Int.read(b)
        
        can_not_skip = True if flags & (1 << 0) else False
        id = Int.read(b)
        
        version = String.read(b)
        
        text = String.read(b)
        
        entities = TLObject.read(b)
        
        document = TLObject.read(b) if flags & (1 << 1) else None
        
        url = String.read(b) if flags & (1 << 2) else None
        sticker = TLObject.read(b) if flags & (1 << 3) else None
        
        return AppUpdate(id=id, version=version, text=text, entities=entities, can_not_skip=can_not_skip, document=document, url=url, sticker=sticker)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.can_not_skip else 0
        flags |= (1 << 1) if self.document is not None else 0
        flags |= (1 << 2) if self.url is not None else 0
        flags |= (1 << 3) if self.sticker is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(String(self.version))
        
        b.write(String(self.text))
        
        b.write(Vector(self.entities))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.url is not None:
            b.write(String(self.url))
        
        if self.sticker is not None:
            b.write(self.sticker.write())
        
        return b.getvalue()

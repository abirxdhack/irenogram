
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BotApp(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotApp`.

    Details:
        - Layer: ``224``
        - ID: ``95FCD1D6``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        access_hash (``int`` ``64-bit``):
            N/A

        short_name (``str``):
            N/A

        title (``str``):
            N/A

        description (``str``):
            N/A

        photo (:obj:`Photo <pyrogram.raw.base.Photo>`):
            N/A

        hash (``int`` ``64-bit``):
            N/A

        document (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "access_hash", "short_name", "title", "description", "photo", "hash", "document"]

    ID = 0x95fcd1d6
    QUALNAME = "types.BotApp"

    def __init__(self, *, id: int, access_hash: int, short_name: str, title: str, description: str, photo: "raw.base.Photo", hash: int, document: "raw.base.Document" = None) -> None:
        self.id = id
        self.access_hash = access_hash
        self.short_name = short_name
        self.title = title
        self.description = description
        self.photo = photo
        self.hash = hash
        self.document = document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotApp":
        
        flags = Int.read(b)
        
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        short_name = String.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        photo = TLObject.read(b)
        
        document = TLObject.read(b) if flags & (1 << 0) else None
        
        hash = Long.read(b)
        
        return BotApp(id=id, access_hash=access_hash, short_name=short_name, title=title, description=description, photo=photo, hash=hash, document=document)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.document is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(String(self.short_name))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        b.write(self.photo.write())
        
        if self.document is not None:
            b.write(self.document.write())
        
        b.write(Long(self.hash))
        
        return b.getvalue()

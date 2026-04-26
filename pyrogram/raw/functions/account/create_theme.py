
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CreateTheme(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``652E4400``

    Parameters:
        slug (``str``):
            N/A

        title (``str``):
            N/A

        document (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`, *optional*):
            N/A

        settings (List of :obj:`InputThemeSettings <pyrogram.raw.base.InputThemeSettings>`, *optional*):
            N/A

    Returns:
        :obj:`Theme <pyrogram.raw.base.Theme>`
    """

    __slots__: List[str] = ["slug", "title", "document", "settings"]

    ID = 0x652e4400
    QUALNAME = "functions.account.CreateTheme"

    def __init__(self, *, slug: str, title: str, document: "raw.base.InputDocument" = None, settings: Optional[List["raw.base.InputThemeSettings"]] = None) -> None:
        self.slug = slug
        self.title = title
        self.document = document
        self.settings = settings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateTheme":
        
        flags = Int.read(b)
        
        slug = String.read(b)
        
        title = String.read(b)
        
        document = TLObject.read(b) if flags & (1 << 2) else None
        
        settings = TLObject.read(b) if flags & (1 << 3) else []
        
        return CreateTheme(slug=slug, title=title, document=document, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.document is not None else 0
        flags |= (1 << 3) if self.settings else 0
        b.write(Int(flags))
        
        b.write(String(self.slug))
        
        b.write(String(self.title))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.settings is not None:
            b.write(Vector(self.settings))
        
        return b.getvalue()

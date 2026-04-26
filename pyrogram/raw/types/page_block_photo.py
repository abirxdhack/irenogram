
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PageBlockPhoto(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``1759C560``

    Parameters:
        photo_id (``int`` ``64-bit``):
            N/A

        caption (:obj:`PageCaption <pyrogram.raw.base.PageCaption>`):
            N/A

        url (``str``, *optional*):
            N/A

        webpage_id (``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["photo_id", "caption", "url", "webpage_id"]

    ID = 0x1759c560
    QUALNAME = "types.PageBlockPhoto"

    def __init__(self, *, photo_id: int, caption: "raw.base.PageCaption", url: Optional[str] = None, webpage_id: Optional[int] = None) -> None:
        self.photo_id = photo_id
        self.caption = caption
        self.url = url
        self.webpage_id = webpage_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockPhoto":
        
        flags = Int.read(b)
        
        photo_id = Long.read(b)
        
        caption = TLObject.read(b)
        
        url = String.read(b) if flags & (1 << 0) else None
        webpage_id = Long.read(b) if flags & (1 << 0) else None
        return PageBlockPhoto(photo_id=photo_id, caption=caption, url=url, webpage_id=webpage_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.url is not None else 0
        flags |= (1 << 0) if self.webpage_id is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.photo_id))
        
        b.write(self.caption.write())
        
        if self.url is not None:
            b.write(String(self.url))
        
        if self.webpage_id is not None:
            b.write(Long(self.webpage_id))
        
        return b.getvalue()

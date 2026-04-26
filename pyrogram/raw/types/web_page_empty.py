
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class WebPageEmpty(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.WebPage`.

    Details:
        - Layer: ``224``
        - ID: ``211A1788``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        url (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "url"]

    ID = 0x211a1788
    QUALNAME = "types.WebPageEmpty"

    def __init__(self, *, id: int, url: Optional[str] = None) -> None:
        self.id = id
        self.url = url

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageEmpty":
        
        flags = Int.read(b)
        
        id = Long.read(b)
        
        url = String.read(b) if flags & (1 << 0) else None
        return WebPageEmpty(id=id, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.url is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        if self.url is not None:
            b.write(String(self.url))
        
        return b.getvalue()

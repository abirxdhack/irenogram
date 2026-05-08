
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMediaPhotoExternal(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``E5BBFE1A``

    Parameters:
        url (``str``):
            N/A

        spoiler (``bool``, *optional*):
            N/A

        ttl_seconds (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["url", "spoiler", "ttl_seconds"]

    ID = 0xe5bbfe1a
    QUALNAME = "types.InputMediaPhotoExternal"

    def __init__(self, *, url: str, spoiler: Optional[bool] = None, ttl_seconds: Optional[int] = None) -> None:
        self.url = url
        self.spoiler = spoiler
        self.ttl_seconds = ttl_seconds

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaPhotoExternal":
        
        flags = Int.read(b)
        
        spoiler = True if flags & (1 << 1) else False
        url = String.read(b)
        
        ttl_seconds = Int.read(b) if flags & (1 << 0) else None
        return InputMediaPhotoExternal(url=url, spoiler=spoiler, ttl_seconds=ttl_seconds)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.spoiler else 0
        flags |= (1 << 0) if self.ttl_seconds is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.url))
        
        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))
        
        return b.getvalue()

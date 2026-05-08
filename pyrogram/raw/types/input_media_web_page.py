
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMediaWebPage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``C21B8849``

    Parameters:
        url (``str``):
            N/A

        force_large_media (``bool``, *optional*):
            N/A

        force_small_media (``bool``, *optional*):
            N/A

        optional (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["url", "force_large_media", "force_small_media", "optional"]

    ID = 0xc21b8849
    QUALNAME = "types.InputMediaWebPage"

    def __init__(self, *, url: str, force_large_media: Optional[bool] = None, force_small_media: Optional[bool] = None, optional: Optional[bool] = None) -> None:
        self.url = url
        self.force_large_media = force_large_media
        self.force_small_media = force_small_media
        self.optional = optional

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaWebPage":
        
        flags = Int.read(b)
        
        force_large_media = True if flags & (1 << 0) else False
        force_small_media = True if flags & (1 << 1) else False
        optional = True if flags & (1 << 2) else False
        url = String.read(b)
        
        return InputMediaWebPage(url=url, force_large_media=force_large_media, force_small_media=force_small_media, optional=optional)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.force_large_media else 0
        flags |= (1 << 1) if self.force_small_media else 0
        flags |= (1 << 2) if self.optional else 0
        b.write(Int(flags))
        
        b.write(String(self.url))
        
        return b.getvalue()

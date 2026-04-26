
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageMediaWebPage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``224``
        - ID: ``DDF10C3B``

    Parameters:
        webpage (:obj:`WebPage <pyrogram.raw.base.WebPage>`):
            N/A

        force_large_media (``bool``, *optional*):
            N/A

        force_small_media (``bool``, *optional*):
            N/A

        manual (``bool``, *optional*):
            N/A

        safe (``bool``, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["webpage", "force_large_media", "force_small_media", "manual", "safe"]

    ID = 0xddf10c3b
    QUALNAME = "types.MessageMediaWebPage"

    def __init__(self, *, webpage: "raw.base.WebPage", force_large_media: Optional[bool] = None, force_small_media: Optional[bool] = None, manual: Optional[bool] = None, safe: Optional[bool] = None) -> None:
        self.webpage = webpage
        self.force_large_media = force_large_media
        self.force_small_media = force_small_media
        self.manual = manual
        self.safe = safe

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaWebPage":
        
        flags = Int.read(b)
        
        force_large_media = True if flags & (1 << 0) else False
        force_small_media = True if flags & (1 << 1) else False
        manual = True if flags & (1 << 3) else False
        safe = True if flags & (1 << 4) else False
        webpage = TLObject.read(b)
        
        return MessageMediaWebPage(webpage=webpage, force_large_media=force_large_media, force_small_media=force_small_media, manual=manual, safe=safe)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.force_large_media else 0
        flags |= (1 << 1) if self.force_small_media else 0
        flags |= (1 << 3) if self.manual else 0
        flags |= (1 << 4) if self.safe else 0
        b.write(Int(flags))
        
        b.write(self.webpage.write())
        
        return b.getvalue()

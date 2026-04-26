
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RecentMeUrlStickerSet(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.RecentMeUrl`.

    Details:
        - Layer: ``224``
        - ID: ``BC0A57DC``

    Parameters:
        url (``str``):
            N/A

        set (:obj:`StickerSetCovered <pyrogram.raw.base.StickerSetCovered>`):
            N/A

    """

    __slots__: List[str] = ["url", "set"]

    ID = 0xbc0a57dc
    QUALNAME = "types.RecentMeUrlStickerSet"

    def __init__(self, *, url: str, set: "raw.base.StickerSetCovered") -> None:
        self.url = url
        self.set = set

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RecentMeUrlStickerSet":
        
        url = String.read(b)
        
        set = TLObject.read(b)
        
        return RecentMeUrlStickerSet(url=url, set=set)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.url))
        
        b.write(self.set.write())
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetRecentMeUrls(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``3DC0F114``

    Parameters:
        referer (``str``):
            N/A

    Returns:
        :obj:`help.RecentMeUrls <pyrogram.raw.base.help.RecentMeUrls>`
    """

    __slots__: List[str] = ["referer"]

    ID = 0x3dc0f114
    QUALNAME = "functions.help.GetRecentMeUrls"

    def __init__(self, *, referer: str) -> None:
        self.referer = referer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetRecentMeUrls":
        
        referer = String.read(b)
        
        return GetRecentMeUrls(referer=referer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.referer))
        
        return b.getvalue()

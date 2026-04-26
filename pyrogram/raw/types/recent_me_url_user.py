
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RecentMeUrlUser(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.RecentMeUrl`.

    Details:
        - Layer: ``224``
        - ID: ``B92C09E2``

    Parameters:
        url (``str``):
            N/A

        user_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["url", "user_id"]

    ID = 0xb92c09e2
    QUALNAME = "types.RecentMeUrlUser"

    def __init__(self, *, url: str, user_id: int) -> None:
        self.url = url
        self.user_id = user_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RecentMeUrlUser":
        
        url = String.read(b)
        
        user_id = Long.read(b)
        
        return RecentMeUrlUser(url=url, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.url))
        
        b.write(Long(self.user_id))
        
        return b.getvalue()

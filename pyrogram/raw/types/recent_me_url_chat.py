
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RecentMeUrlChat(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.RecentMeUrl`.

    Details:
        - Layer: ``224``
        - ID: ``B2DA71D2``

    Parameters:
        url (``str``):
            N/A

        chat_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["url", "chat_id"]

    ID = 0xb2da71d2
    QUALNAME = "types.RecentMeUrlChat"

    def __init__(self, *, url: str, chat_id: int) -> None:
        self.url = url
        self.chat_id = chat_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RecentMeUrlChat":
        
        url = String.read(b)
        
        chat_id = Long.read(b)
        
        return RecentMeUrlChat(url=url, chat_id=chat_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.url))
        
        b.write(Long(self.chat_id))
        
        return b.getvalue()

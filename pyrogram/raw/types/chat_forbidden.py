
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChatForbidden(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Chat`.

    Details:
        - Layer: ``224``
        - ID: ``6592A1A7``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        title (``str``):
            N/A

    """

    __slots__: List[str] = ["id", "title"]

    ID = 0x6592a1a7
    QUALNAME = "types.ChatForbidden"

    def __init__(self, *, id: int, title: str) -> None:
        self.id = id
        self.title = title

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatForbidden":
        
        id = Long.read(b)
        
        title = String.read(b)
        
        return ChatForbidden(id=id, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        
        b.write(String(self.title))
        
        return b.getvalue()

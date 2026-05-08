
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageEntityTextUrl(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageEntity`.

    Details:
        - Layer: ``224``
        - ID: ``76A6D327``

    Parameters:
        offset (``int`` ``32-bit``):
            N/A

        length (``int`` ``32-bit``):
            N/A

        url (``str``):
            N/A

    """

    __slots__: List[str] = ["offset", "length", "url"]

    ID = 0x76a6d327
    QUALNAME = "types.MessageEntityTextUrl"

    def __init__(self, *, offset: int, length: int, url: str) -> None:
        self.offset = offset
        self.length = length
        self.url = url

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEntityTextUrl":
        
        offset = Int.read(b)
        
        length = Int.read(b)
        
        url = String.read(b)
        
        return MessageEntityTextUrl(offset=offset, length=length, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.offset))
        
        b.write(Int(self.length))
        
        b.write(String(self.url))
        
        return b.getvalue()

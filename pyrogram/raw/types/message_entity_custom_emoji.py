
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageEntityCustomEmoji(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageEntity`.

    Details:
        - Layer: ``224``
        - ID: ``C8CF05F8``

    Parameters:
        offset (``int`` ``32-bit``):
            N/A

        length (``int`` ``32-bit``):
            N/A

        document_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["offset", "length", "document_id"]

    ID = 0xc8cf05f8
    QUALNAME = "types.MessageEntityCustomEmoji"

    def __init__(self, *, offset: int, length: int, document_id: int) -> None:
        self.offset = offset
        self.length = length
        self.document_id = document_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEntityCustomEmoji":
        
        offset = Int.read(b)
        
        length = Int.read(b)
        
        document_id = Long.read(b)
        
        return MessageEntityCustomEmoji(offset=offset, length=length, document_id=document_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.offset))
        
        b.write(Int(self.length))
        
        b.write(Long(self.document_id))
        
        return b.getvalue()

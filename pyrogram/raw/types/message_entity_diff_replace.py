
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageEntityDiffReplace(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageEntity`.

    Details:
        - Layer: ``224``
        - ID: ``C6C1E5A7``

    Parameters:
        offset (``int`` ``32-bit``):
            N/A

        length (``int`` ``32-bit``):
            N/A

        old_text (``str``):
            N/A

    """

    __slots__: List[str] = ["offset", "length", "old_text"]

    ID = 0xc6c1e5a7
    QUALNAME = "types.MessageEntityDiffReplace"

    def __init__(self, *, offset: int, length: int, old_text: str) -> None:
        self.offset = offset
        self.length = length
        self.old_text = old_text

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEntityDiffReplace":
        
        offset = Int.read(b)
        
        length = Int.read(b)
        
        old_text = String.read(b)
        
        return MessageEntityDiffReplace(offset=offset, length=length, old_text=old_text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.offset))
        
        b.write(Int(self.length))
        
        b.write(String(self.old_text))
        
        return b.getvalue()

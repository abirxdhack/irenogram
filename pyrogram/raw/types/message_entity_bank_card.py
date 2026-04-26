
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageEntityBankCard(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageEntity`.

    Details:
        - Layer: ``224``
        - ID: ``761E6AF4``

    Parameters:
        offset (``int`` ``32-bit``):
            N/A

        length (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["offset", "length"]

    ID = 0x761e6af4
    QUALNAME = "types.MessageEntityBankCard"

    def __init__(self, *, offset: int, length: int) -> None:
        self.offset = offset
        self.length = length

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEntityBankCard":
        
        offset = Int.read(b)
        
        length = Int.read(b)
        
        return MessageEntityBankCard(offset=offset, length=length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.offset))
        
        b.write(Int(self.length))
        
        return b.getvalue()

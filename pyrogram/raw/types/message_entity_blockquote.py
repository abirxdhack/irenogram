
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageEntityBlockquote(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageEntity`.

    Details:
        - Layer: ``224``
        - ID: ``F1CCAAAC``

    Parameters:
        offset (``int`` ``32-bit``):
            N/A

        length (``int`` ``32-bit``):
            N/A

        collapsed (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["offset", "length", "collapsed"]

    ID = 0xf1ccaaac
    QUALNAME = "types.MessageEntityBlockquote"

    def __init__(self, *, offset: int, length: int, collapsed: Optional[bool] = None) -> None:
        self.offset = offset
        self.length = length
        self.collapsed = collapsed

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEntityBlockquote":
        
        flags = Int.read(b)
        
        collapsed = True if flags & (1 << 0) else False
        offset = Int.read(b)
        
        length = Int.read(b)
        
        return MessageEntityBlockquote(offset=offset, length=length, collapsed=collapsed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.collapsed else 0
        b.write(Int(flags))
        
        b.write(Int(self.offset))
        
        b.write(Int(self.length))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EmojiStatus(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.EmojiStatus`.

    Details:
        - Layer: ``224``
        - ID: ``E7FF068A``

    Parameters:
        document_id (``int`` ``64-bit``):
            N/A

        until (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["document_id", "until"]

    ID = 0xe7ff068a
    QUALNAME = "types.EmojiStatus"

    def __init__(self, *, document_id: int, until: Optional[int] = None) -> None:
        self.document_id = document_id
        self.until = until

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiStatus":
        
        flags = Int.read(b)
        
        document_id = Long.read(b)
        
        until = Int.read(b) if flags & (1 << 0) else None
        return EmojiStatus(document_id=document_id, until=until)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.until is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.document_id))
        
        if self.until is not None:
            b.write(Int(self.until))
        
        return b.getvalue()

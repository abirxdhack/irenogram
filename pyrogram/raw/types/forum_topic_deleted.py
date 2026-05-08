
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ForumTopicDeleted(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ForumTopic`.

    Details:
        - Layer: ``224``
        - ID: ``23F109B``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["id"]

    ID = 0x23f109b
    QUALNAME = "types.ForumTopicDeleted"

    def __init__(self, *, id: int) -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ForumTopicDeleted":
        
        id = Int.read(b)
        
        return ForumTopicDeleted(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.id))
        
        return b.getvalue()

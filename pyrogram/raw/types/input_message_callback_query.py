
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMessageCallbackQuery(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMessage`.

    Details:
        - Layer: ``224``
        - ID: ``ACFA1A7E``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        query_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["id", "query_id"]

    ID = 0xacfa1a7e
    QUALNAME = "types.InputMessageCallbackQuery"

    def __init__(self, *, id: int, query_id: int) -> None:
        self.id = id
        self.query_id = query_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMessageCallbackQuery":
        
        id = Int.read(b)
        
        query_id = Long.read(b)
        
        return InputMessageCallbackQuery(id=id, query_id=query_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.id))
        
        b.write(Long(self.query_id))
        
        return b.getvalue()

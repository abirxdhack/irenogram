
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMessageID(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMessage`.

    Details:
        - Layer: ``224``
        - ID: ``A676A322``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["id"]

    ID = 0xa676a322
    QUALNAME = "types.InputMessageID"

    def __init__(self, *, id: int) -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMessageID":
        
        id = Int.read(b)
        
        return InputMessageID(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.id))
        
        return b.getvalue()

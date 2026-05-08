
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputWallPaperNoFile(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputWallPaper`.

    Details:
        - Layer: ``224``
        - ID: ``967A462E``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["id"]

    ID = 0x967a462e
    QUALNAME = "types.InputWallPaperNoFile"

    def __init__(self, *, id: int) -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputWallPaperNoFile":
        
        id = Long.read(b)
        
        return InputWallPaperNoFile(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        
        return b.getvalue()

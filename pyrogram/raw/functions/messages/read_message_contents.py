
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReadMessageContents(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``36A73F77``

    Parameters:
        id (List of ``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.AffectedMessages <pyrogram.raw.base.messages.AffectedMessages>`
    """

    __slots__: List[str] = ["id"]

    ID = 0x36a73f77
    QUALNAME = "functions.messages.ReadMessageContents"

    def __init__(self, *, id: List[int]) -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReadMessageContents":
        
        id = TLObject.read(b, Int)
        
        return ReadMessageContents(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.id, Int))
        
        return b.getvalue()

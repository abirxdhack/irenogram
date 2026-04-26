
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class Timezone(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Timezone`.

    Details:
        - Layer: ``224``
        - ID: ``FF9289F5``

    Parameters:
        id (``str``):
            N/A

        name (``str``):
            N/A

        utc_offset (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["id", "name", "utc_offset"]

    ID = 0xff9289f5
    QUALNAME = "types.Timezone"

    def __init__(self, *, id: str, name: str, utc_offset: int) -> None:
        self.id = id
        self.name = name
        self.utc_offset = utc_offset

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Timezone":
        
        id = String.read(b)
        
        name = String.read(b)
        
        utc_offset = Int.read(b)
        
        return Timezone(id=id, name=name, utc_offset=utc_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.id))
        
        b.write(String(self.name))
        
        b.write(Int(self.utc_offset))
        
        return b.getvalue()

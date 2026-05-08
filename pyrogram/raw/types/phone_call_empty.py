
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PhoneCallEmpty(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PhoneCall`.

    Details:
        - Layer: ``224``
        - ID: ``5366C915``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["id"]

    ID = 0x5366c915
    QUALNAME = "types.PhoneCallEmpty"

    def __init__(self, *, id: int) -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneCallEmpty":
        
        id = Long.read(b)
        
        return PhoneCallEmpty(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        
        return b.getvalue()

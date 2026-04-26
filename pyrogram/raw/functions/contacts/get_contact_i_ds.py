
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetContactIDs(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``7ADC669D``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

    Returns:
        List of ``int`` ``32-bit``
    """

    __slots__: List[str] = ["hash"]

    ID = 0x7adc669d
    QUALNAME = "functions.contacts.GetContactIDs"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetContactIDs":
        
        hash = Long.read(b)
        
        return GetContactIDs(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        return b.getvalue()

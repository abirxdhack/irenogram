
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetContacts(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``5DD69E12``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`contacts.Contacts <pyrogram.raw.base.contacts.Contacts>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x5dd69e12
    QUALNAME = "functions.contacts.GetContacts"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetContacts":
        
        hash = Long.read(b)
        
        return GetContacts(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        return b.getvalue()

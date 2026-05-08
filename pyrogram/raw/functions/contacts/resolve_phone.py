
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ResolvePhone(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``8AF94344``

    Parameters:
        phone (``str``):
            N/A

    Returns:
        :obj:`contacts.ResolvedPeer <pyrogram.raw.base.contacts.ResolvedPeer>`
    """

    __slots__: List[str] = ["phone"]

    ID = 0x8af94344
    QUALNAME = "functions.contacts.ResolvePhone"

    def __init__(self, *, phone: str) -> None:
        self.phone = phone

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResolvePhone":
        
        phone = String.read(b)
        
        return ResolvePhone(phone=phone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.phone))
        
        return b.getvalue()

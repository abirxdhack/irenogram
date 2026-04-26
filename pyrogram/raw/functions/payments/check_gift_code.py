
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CheckGiftCode(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``8E51B4C1``

    Parameters:
        slug (``str``):
            N/A

    Returns:
        :obj:`payments.CheckedGiftCode <pyrogram.raw.base.payments.CheckedGiftCode>`
    """

    __slots__: List[str] = ["slug"]

    ID = 0x8e51b4c1
    QUALNAME = "functions.payments.CheckGiftCode"

    def __init__(self, *, slug: str) -> None:
        self.slug = slug

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckGiftCode":
        
        slug = String.read(b)
        
        return CheckGiftCode(slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.slug))
        
        return b.getvalue()

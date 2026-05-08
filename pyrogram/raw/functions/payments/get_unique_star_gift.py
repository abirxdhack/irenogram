
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetUniqueStarGift(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A1974D72``

    Parameters:
        slug (``str``):
            N/A

    Returns:
        :obj:`payments.UniqueStarGift <pyrogram.raw.base.payments.UniqueStarGift>`
    """

    __slots__: List[str] = ["slug"]

    ID = 0xa1974d72
    QUALNAME = "functions.payments.GetUniqueStarGift"

    def __init__(self, *, slug: str) -> None:
        self.slug = slug

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUniqueStarGift":
        
        slug = String.read(b)
        
        return GetUniqueStarGift(slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.slug))
        
        return b.getvalue()

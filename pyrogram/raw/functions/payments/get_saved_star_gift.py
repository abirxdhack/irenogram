
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetSavedStarGift(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``B455A106``

    Parameters:
        stargift (List of :obj:`InputSavedStarGift <pyrogram.raw.base.InputSavedStarGift>`):
            N/A

    Returns:
        :obj:`payments.SavedStarGifts <pyrogram.raw.base.payments.SavedStarGifts>`
    """

    __slots__: List[str] = ["stargift"]

    ID = 0xb455a106
    QUALNAME = "functions.payments.GetSavedStarGift"

    def __init__(self, *, stargift: List["raw.base.InputSavedStarGift"]) -> None:
        self.stargift = stargift

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSavedStarGift":
        
        stargift = TLObject.read(b)
        
        return GetSavedStarGift(stargift=stargift)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.stargift))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetPromoData(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``C0977421``

    Parameters:
        No parameters required.

    Returns:
        :obj:`help.PromoData <pyrogram.raw.base.help.PromoData>`
    """

    __slots__: List[str] = []

    ID = 0xc0977421
    QUALNAME = "functions.help.GetPromoData"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPromoData":
        
        return GetPromoData()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

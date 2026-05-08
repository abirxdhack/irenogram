
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetStarGiftUpgradeAttributes(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``6D038B58``

    Parameters:
        gift_id (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`payments.StarGiftUpgradeAttributes <pyrogram.raw.base.payments.StarGiftUpgradeAttributes>`
    """

    __slots__: List[str] = ["gift_id"]

    ID = 0x6d038b58
    QUALNAME = "functions.payments.GetStarGiftUpgradeAttributes"

    def __init__(self, *, gift_id: int) -> None:
        self.gift_id = gift_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarGiftUpgradeAttributes":
        
        gift_id = Long.read(b)
        
        return GetStarGiftUpgradeAttributes(gift_id=gift_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.gift_id))
        
        return b.getvalue()

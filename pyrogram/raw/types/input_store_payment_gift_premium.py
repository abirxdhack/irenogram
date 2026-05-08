
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputStorePaymentGiftPremium(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputStorePaymentPurpose`.

    Details:
        - Layer: ``224``
        - ID: ``616F7FE8``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        currency (``str``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["user_id", "currency", "amount"]

    ID = 0x616f7fe8
    QUALNAME = "types.InputStorePaymentGiftPremium"

    def __init__(self, *, user_id: "raw.base.InputUser", currency: str, amount: int) -> None:
        self.user_id = user_id
        self.currency = currency
        self.amount = amount

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStorePaymentGiftPremium":
        
        user_id = TLObject.read(b)
        
        currency = String.read(b)
        
        amount = Long.read(b)
        
        return InputStorePaymentGiftPremium(user_id=user_id, currency=currency, amount=amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.user_id.write())
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        return b.getvalue()

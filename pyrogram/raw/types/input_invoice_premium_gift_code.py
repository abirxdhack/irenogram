
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputInvoicePremiumGiftCode(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``224``
        - ID: ``98986C0D``

    Parameters:
        purpose (:obj:`InputStorePaymentPurpose <pyrogram.raw.base.InputStorePaymentPurpose>`):
            N/A

        option (:obj:`PremiumGiftCodeOption <pyrogram.raw.base.PremiumGiftCodeOption>`):
            N/A

    """

    __slots__: List[str] = ["purpose", "option"]

    ID = 0x98986c0d
    QUALNAME = "types.InputInvoicePremiumGiftCode"

    def __init__(self, *, purpose: "raw.base.InputStorePaymentPurpose", option: "raw.base.PremiumGiftCodeOption") -> None:
        self.purpose = purpose
        self.option = option

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoicePremiumGiftCode":
        
        purpose = TLObject.read(b)
        
        option = TLObject.read(b)
        
        return InputInvoicePremiumGiftCode(purpose=purpose, option=option)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.purpose.write())
        
        b.write(self.option.write())
        
        return b.getvalue()

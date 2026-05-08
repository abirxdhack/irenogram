
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputInvoicePremiumAuthCode(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``224``
        - ID: ``3E77F614``

    Parameters:
        purpose (:obj:`InputStorePaymentPurpose <pyrogram.raw.base.InputStorePaymentPurpose>`):
            N/A

    """

    __slots__: List[str] = ["purpose"]

    ID = 0x3e77f614
    QUALNAME = "types.InputInvoicePremiumAuthCode"

    def __init__(self, *, purpose: "raw.base.InputStorePaymentPurpose") -> None:
        self.purpose = purpose

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoicePremiumAuthCode":
        
        purpose = TLObject.read(b)
        
        return InputInvoicePremiumAuthCode(purpose=purpose)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.purpose.write())
        
        return b.getvalue()

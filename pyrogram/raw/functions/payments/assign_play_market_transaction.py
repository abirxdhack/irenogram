
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AssignPlayMarketTransaction(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``DFFD50D3``

    Parameters:
        receipt (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            N/A

        purpose (:obj:`InputStorePaymentPurpose <pyrogram.raw.base.InputStorePaymentPurpose>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["receipt", "purpose"]

    ID = 0xdffd50d3
    QUALNAME = "functions.payments.AssignPlayMarketTransaction"

    def __init__(self, *, receipt: "raw.base.DataJSON", purpose: "raw.base.InputStorePaymentPurpose") -> None:
        self.receipt = receipt
        self.purpose = purpose

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AssignPlayMarketTransaction":
        
        receipt = TLObject.read(b)
        
        purpose = TLObject.read(b)
        
        return AssignPlayMarketTransaction(receipt=receipt, purpose=purpose)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.receipt.write())
        
        b.write(self.purpose.write())
        
        return b.getvalue()

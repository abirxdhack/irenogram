
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputInvoiceStars(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``224``
        - ID: ``65F00CE3``

    Parameters:
        purpose (:obj:`InputStorePaymentPurpose <pyrogram.raw.base.InputStorePaymentPurpose>`):
            N/A

    """

    __slots__: List[str] = ["purpose"]

    ID = 0x65f00ce3
    QUALNAME = "types.InputInvoiceStars"

    def __init__(self, *, purpose: "raw.base.InputStorePaymentPurpose") -> None:
        self.purpose = purpose

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceStars":
        
        purpose = TLObject.read(b)
        
        return InputInvoiceStars(purpose=purpose)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.purpose.write())
        
        return b.getvalue()

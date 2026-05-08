
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SendStarsForm(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``7998C914``

    Parameters:
        form_id (``int`` ``64-bit``):
            N/A

        invoice (:obj:`InputInvoice <pyrogram.raw.base.InputInvoice>`):
            N/A

    Returns:
        :obj:`payments.PaymentResult <pyrogram.raw.base.payments.PaymentResult>`
    """

    __slots__: List[str] = ["form_id", "invoice"]

    ID = 0x7998c914
    QUALNAME = "functions.payments.SendStarsForm"

    def __init__(self, *, form_id: int, invoice: "raw.base.InputInvoice") -> None:
        self.form_id = form_id
        self.invoice = invoice

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendStarsForm":
        
        form_id = Long.read(b)
        
        invoice = TLObject.read(b)
        
        return SendStarsForm(form_id=form_id, invoice=invoice)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.form_id))
        
        b.write(self.invoice.write())
        
        return b.getvalue()

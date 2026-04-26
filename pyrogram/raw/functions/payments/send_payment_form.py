
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SendPaymentForm(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``2D03522F``

    Parameters:
        form_id (``int`` ``64-bit``):
            N/A

        invoice (:obj:`InputInvoice <pyrogram.raw.base.InputInvoice>`):
            N/A

        credentials (:obj:`InputPaymentCredentials <pyrogram.raw.base.InputPaymentCredentials>`):
            N/A

        requested_info_id (``str``, *optional*):
            N/A

        shipping_option_id (``str``, *optional*):
            N/A

        tip_amount (``int`` ``64-bit``, *optional*):
            N/A

    Returns:
        :obj:`payments.PaymentResult <pyrogram.raw.base.payments.PaymentResult>`
    """

    __slots__: List[str] = ["form_id", "invoice", "credentials", "requested_info_id", "shipping_option_id", "tip_amount"]

    ID = 0x2d03522f
    QUALNAME = "functions.payments.SendPaymentForm"

    def __init__(self, *, form_id: int, invoice: "raw.base.InputInvoice", credentials: "raw.base.InputPaymentCredentials", requested_info_id: Optional[str] = None, shipping_option_id: Optional[str] = None, tip_amount: Optional[int] = None) -> None:
        self.form_id = form_id
        self.invoice = invoice
        self.credentials = credentials
        self.requested_info_id = requested_info_id
        self.shipping_option_id = shipping_option_id
        self.tip_amount = tip_amount

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendPaymentForm":
        
        flags = Int.read(b)
        
        form_id = Long.read(b)
        
        invoice = TLObject.read(b)
        
        requested_info_id = String.read(b) if flags & (1 << 0) else None
        shipping_option_id = String.read(b) if flags & (1 << 1) else None
        credentials = TLObject.read(b)
        
        tip_amount = Long.read(b) if flags & (1 << 2) else None
        return SendPaymentForm(form_id=form_id, invoice=invoice, credentials=credentials, requested_info_id=requested_info_id, shipping_option_id=shipping_option_id, tip_amount=tip_amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.requested_info_id is not None else 0
        flags |= (1 << 1) if self.shipping_option_id is not None else 0
        flags |= (1 << 2) if self.tip_amount is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.form_id))
        
        b.write(self.invoice.write())
        
        if self.requested_info_id is not None:
            b.write(String(self.requested_info_id))
        
        if self.shipping_option_id is not None:
            b.write(String(self.shipping_option_id))
        
        b.write(self.credentials.write())
        
        if self.tip_amount is not None:
            b.write(Long(self.tip_amount))
        
        return b.getvalue()

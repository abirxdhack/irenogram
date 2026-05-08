
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ValidateRequestedInfo(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``B6C8F12B``

    Parameters:
        invoice (:obj:`InputInvoice <pyrogram.raw.base.InputInvoice>`):
            N/A

        info (:obj:`PaymentRequestedInfo <pyrogram.raw.base.PaymentRequestedInfo>`):
            N/A

        save (``bool``, *optional*):
            N/A

    Returns:
        :obj:`payments.ValidatedRequestedInfo <pyrogram.raw.base.payments.ValidatedRequestedInfo>`
    """

    __slots__: List[str] = ["invoice", "info", "save"]

    ID = 0xb6c8f12b
    QUALNAME = "functions.payments.ValidateRequestedInfo"

    def __init__(self, *, invoice: "raw.base.InputInvoice", info: "raw.base.PaymentRequestedInfo", save: Optional[bool] = None) -> None:
        self.invoice = invoice
        self.info = info
        self.save = save

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ValidateRequestedInfo":
        
        flags = Int.read(b)
        
        save = True if flags & (1 << 0) else False
        invoice = TLObject.read(b)
        
        info = TLObject.read(b)
        
        return ValidateRequestedInfo(invoice=invoice, info=info, save=save)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.save else 0
        b.write(Int(flags))
        
        b.write(self.invoice.write())
        
        b.write(self.info.write())
        
        return b.getvalue()

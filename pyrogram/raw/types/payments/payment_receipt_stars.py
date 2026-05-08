
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PaymentReceiptStars(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.PaymentReceipt`.

    Details:
        - Layer: ``224``
        - ID: ``DABBF83A``

    Parameters:
        date (``int`` ``32-bit``):
            N/A

        bot_id (``int`` ``64-bit``):
            N/A

        title (``str``):
            N/A

        description (``str``):
            N/A

        invoice (:obj:`Invoice <pyrogram.raw.base.Invoice>`):
            N/A

        currency (``str``):
            N/A

        total_amount (``int`` ``64-bit``):
            N/A

        transaction_id (``str``):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        photo (:obj:`WebDocument <pyrogram.raw.base.WebDocument>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetPaymentReceipt
    """

    __slots__: List[str] = ["date", "bot_id", "title", "description", "invoice", "currency", "total_amount", "transaction_id", "users", "photo"]

    ID = 0xdabbf83a
    QUALNAME = "types.payments.PaymentReceiptStars"

    def __init__(self, *, date: int, bot_id: int, title: str, description: str, invoice: "raw.base.Invoice", currency: str, total_amount: int, transaction_id: str, users: List["raw.base.User"], photo: "raw.base.WebDocument" = None) -> None:
        self.date = date
        self.bot_id = bot_id
        self.title = title
        self.description = description
        self.invoice = invoice
        self.currency = currency
        self.total_amount = total_amount
        self.transaction_id = transaction_id
        self.users = users
        self.photo = photo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentReceiptStars":
        
        flags = Int.read(b)
        
        date = Int.read(b)
        
        bot_id = Long.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        photo = TLObject.read(b) if flags & (1 << 2) else None
        
        invoice = TLObject.read(b)
        
        currency = String.read(b)
        
        total_amount = Long.read(b)
        
        transaction_id = String.read(b)
        
        users = TLObject.read(b)
        
        return PaymentReceiptStars(date=date, bot_id=bot_id, title=title, description=description, invoice=invoice, currency=currency, total_amount=total_amount, transaction_id=transaction_id, users=users, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.photo is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.date))
        
        b.write(Long(self.bot_id))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        b.write(self.invoice.write())
        
        b.write(String(self.currency))
        
        b.write(Long(self.total_amount))
        
        b.write(String(self.transaction_id))
        
        b.write(Vector(self.users))
        
        return b.getvalue()

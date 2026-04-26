
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SentCodePaymentRequired(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.auth.SentCode`.

    Details:
        - Layer: ``224``
        - ID: ``E0955A3C``

    Parameters:
        store_product (``str``):
            N/A

        phone_code_hash (``str``):
            N/A

        support_email_address (``str``):
            N/A

        support_email_subject (``str``):
            N/A

        currency (``str``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 7 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.SendCode
            auth.ResendCode
            auth.ResetLoginEmail
            auth.CheckPaidAuth
            account.SendChangePhoneCode
            account.SendConfirmPhoneCode
            account.SendVerifyPhoneCode
    """

    __slots__: List[str] = ["store_product", "phone_code_hash", "support_email_address", "support_email_subject", "currency", "amount"]

    ID = 0xe0955a3c
    QUALNAME = "types.auth.SentCodePaymentRequired"

    def __init__(self, *, store_product: str, phone_code_hash: str, support_email_address: str, support_email_subject: str, currency: str, amount: int) -> None:
        self.store_product = store_product
        self.phone_code_hash = phone_code_hash
        self.support_email_address = support_email_address
        self.support_email_subject = support_email_subject
        self.currency = currency
        self.amount = amount

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodePaymentRequired":
        
        store_product = String.read(b)
        
        phone_code_hash = String.read(b)
        
        support_email_address = String.read(b)
        
        support_email_subject = String.read(b)
        
        currency = String.read(b)
        
        amount = Long.read(b)
        
        return SentCodePaymentRequired(store_product=store_product, phone_code_hash=phone_code_hash, support_email_address=support_email_address, support_email_subject=support_email_subject, currency=currency, amount=amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.store_product))
        
        b.write(String(self.phone_code_hash))
        
        b.write(String(self.support_email_address))
        
        b.write(String(self.support_email_subject))
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        return b.getvalue()

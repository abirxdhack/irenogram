
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class Invoice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Invoice`.

    Details:
        - Layer: ``224``
        - ID: ``49EE584``

    Parameters:
        currency (``str``):
            N/A

        prices (List of :obj:`LabeledPrice <pyrogram.raw.base.LabeledPrice>`):
            N/A

        test (``bool``, *optional*):
            N/A

        name_requested (``bool``, *optional*):
            N/A

        phone_requested (``bool``, *optional*):
            N/A

        email_requested (``bool``, *optional*):
            N/A

        shipping_address_requested (``bool``, *optional*):
            N/A

        flexible (``bool``, *optional*):
            N/A

        phone_to_provider (``bool``, *optional*):
            N/A

        email_to_provider (``bool``, *optional*):
            N/A

        recurring (``bool``, *optional*):
            N/A

        max_tip_amount (``int`` ``64-bit``, *optional*):
            N/A

        suggested_tip_amounts (List of ``int`` ``64-bit``, *optional*):
            N/A

        terms_url (``str``, *optional*):
            N/A

        subscription_period (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["currency", "prices", "test", "name_requested", "phone_requested", "email_requested", "shipping_address_requested", "flexible", "phone_to_provider", "email_to_provider", "recurring", "max_tip_amount", "suggested_tip_amounts", "terms_url", "subscription_period"]

    ID = 0x49ee584
    QUALNAME = "types.Invoice"

    def __init__(self, *, currency: str, prices: List["raw.base.LabeledPrice"], test: Optional[bool] = None, name_requested: Optional[bool] = None, phone_requested: Optional[bool] = None, email_requested: Optional[bool] = None, shipping_address_requested: Optional[bool] = None, flexible: Optional[bool] = None, phone_to_provider: Optional[bool] = None, email_to_provider: Optional[bool] = None, recurring: Optional[bool] = None, max_tip_amount: Optional[int] = None, suggested_tip_amounts: Optional[List[int]] = None, terms_url: Optional[str] = None, subscription_period: Optional[int] = None) -> None:
        self.currency = currency
        self.prices = prices
        self.test = test
        self.name_requested = name_requested
        self.phone_requested = phone_requested
        self.email_requested = email_requested
        self.shipping_address_requested = shipping_address_requested
        self.flexible = flexible
        self.phone_to_provider = phone_to_provider
        self.email_to_provider = email_to_provider
        self.recurring = recurring
        self.max_tip_amount = max_tip_amount
        self.suggested_tip_amounts = suggested_tip_amounts
        self.terms_url = terms_url
        self.subscription_period = subscription_period

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Invoice":
        
        flags = Int.read(b)
        
        test = True if flags & (1 << 0) else False
        name_requested = True if flags & (1 << 1) else False
        phone_requested = True if flags & (1 << 2) else False
        email_requested = True if flags & (1 << 3) else False
        shipping_address_requested = True if flags & (1 << 4) else False
        flexible = True if flags & (1 << 5) else False
        phone_to_provider = True if flags & (1 << 6) else False
        email_to_provider = True if flags & (1 << 7) else False
        recurring = True if flags & (1 << 9) else False
        currency = String.read(b)
        
        prices = TLObject.read(b)
        
        max_tip_amount = Long.read(b) if flags & (1 << 8) else None
        suggested_tip_amounts = TLObject.read(b, Long) if flags & (1 << 8) else []
        
        terms_url = String.read(b) if flags & (1 << 10) else None
        subscription_period = Int.read(b) if flags & (1 << 11) else None
        return Invoice(currency=currency, prices=prices, test=test, name_requested=name_requested, phone_requested=phone_requested, email_requested=email_requested, shipping_address_requested=shipping_address_requested, flexible=flexible, phone_to_provider=phone_to_provider, email_to_provider=email_to_provider, recurring=recurring, max_tip_amount=max_tip_amount, suggested_tip_amounts=suggested_tip_amounts, terms_url=terms_url, subscription_period=subscription_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.test else 0
        flags |= (1 << 1) if self.name_requested else 0
        flags |= (1 << 2) if self.phone_requested else 0
        flags |= (1 << 3) if self.email_requested else 0
        flags |= (1 << 4) if self.shipping_address_requested else 0
        flags |= (1 << 5) if self.flexible else 0
        flags |= (1 << 6) if self.phone_to_provider else 0
        flags |= (1 << 7) if self.email_to_provider else 0
        flags |= (1 << 9) if self.recurring else 0
        flags |= (1 << 8) if self.max_tip_amount is not None else 0
        flags |= (1 << 8) if self.suggested_tip_amounts else 0
        flags |= (1 << 10) if self.terms_url is not None else 0
        flags |= (1 << 11) if self.subscription_period is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.currency))
        
        b.write(Vector(self.prices))
        
        if self.max_tip_amount is not None:
            b.write(Long(self.max_tip_amount))
        
        if self.suggested_tip_amounts is not None:
            b.write(Vector(self.suggested_tip_amounts, Long))
        
        if self.terms_url is not None:
            b.write(String(self.terms_url))
        
        if self.subscription_period is not None:
            b.write(Int(self.subscription_period))
        
        return b.getvalue()

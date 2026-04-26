
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PremiumSubscriptionOption(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PremiumSubscriptionOption`.

    Details:
        - Layer: ``224``
        - ID: ``5F2D1DF2``

    Parameters:
        months (``int`` ``32-bit``):
            N/A

        currency (``str``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

        bot_url (``str``):
            N/A

        current (``bool``, *optional*):
            N/A

        can_purchase_upgrade (``bool``, *optional*):
            N/A

        transaction (``str``, *optional*):
            N/A

        store_product (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["months", "currency", "amount", "bot_url", "current", "can_purchase_upgrade", "transaction", "store_product"]

    ID = 0x5f2d1df2
    QUALNAME = "types.PremiumSubscriptionOption"

    def __init__(self, *, months: int, currency: str, amount: int, bot_url: str, current: Optional[bool] = None, can_purchase_upgrade: Optional[bool] = None, transaction: Optional[str] = None, store_product: Optional[str] = None) -> None:
        self.months = months
        self.currency = currency
        self.amount = amount
        self.bot_url = bot_url
        self.current = current
        self.can_purchase_upgrade = can_purchase_upgrade
        self.transaction = transaction
        self.store_product = store_product

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PremiumSubscriptionOption":
        
        flags = Int.read(b)
        
        current = True if flags & (1 << 1) else False
        can_purchase_upgrade = True if flags & (1 << 2) else False
        transaction = String.read(b) if flags & (1 << 3) else None
        months = Int.read(b)
        
        currency = String.read(b)
        
        amount = Long.read(b)
        
        bot_url = String.read(b)
        
        store_product = String.read(b) if flags & (1 << 0) else None
        return PremiumSubscriptionOption(months=months, currency=currency, amount=amount, bot_url=bot_url, current=current, can_purchase_upgrade=can_purchase_upgrade, transaction=transaction, store_product=store_product)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.current else 0
        flags |= (1 << 2) if self.can_purchase_upgrade else 0
        flags |= (1 << 3) if self.transaction is not None else 0
        flags |= (1 << 0) if self.store_product is not None else 0
        b.write(Int(flags))
        
        if self.transaction is not None:
            b.write(String(self.transaction))
        
        b.write(Int(self.months))
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        b.write(String(self.bot_url))
        
        if self.store_product is not None:
            b.write(String(self.store_product))
        
        return b.getvalue()

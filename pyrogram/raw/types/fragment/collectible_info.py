
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CollectibleInfo(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.fragment.CollectibleInfo`.

    Details:
        - Layer: ``224``
        - ID: ``6EBDFF91``

    Parameters:
        purchase_date (``int`` ``32-bit``):
            N/A

        currency (``str``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

        crypto_currency (``str``):
            N/A

        crypto_amount (``int`` ``64-bit``):
            N/A

        url (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            fragment.GetCollectibleInfo
    """

    __slots__: List[str] = ["purchase_date", "currency", "amount", "crypto_currency", "crypto_amount", "url"]

    ID = 0x6ebdff91
    QUALNAME = "types.fragment.CollectibleInfo"

    def __init__(self, *, purchase_date: int, currency: str, amount: int, crypto_currency: str, crypto_amount: int, url: str) -> None:
        self.purchase_date = purchase_date
        self.currency = currency
        self.amount = amount
        self.crypto_currency = crypto_currency
        self.crypto_amount = crypto_amount
        self.url = url

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CollectibleInfo":
        
        purchase_date = Int.read(b)
        
        currency = String.read(b)
        
        amount = Long.read(b)
        
        crypto_currency = String.read(b)
        
        crypto_amount = Long.read(b)
        
        url = String.read(b)
        
        return CollectibleInfo(purchase_date=purchase_date, currency=currency, amount=amount, crypto_currency=crypto_currency, crypto_amount=crypto_amount, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.purchase_date))
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        b.write(String(self.crypto_currency))
        
        b.write(Long(self.crypto_amount))
        
        b.write(String(self.url))
        
        return b.getvalue()

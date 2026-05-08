
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PaymentVerificationNeeded(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.PaymentResult`.

    Details:
        - Layer: ``224``
        - ID: ``D8411139``

    Parameters:
        url (``str``):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.SendPaymentForm
            payments.SendStarsForm
    """

    __slots__: List[str] = ["url"]

    ID = 0xd8411139
    QUALNAME = "types.payments.PaymentVerificationNeeded"

    def __init__(self, *, url: str) -> None:
        self.url = url

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentVerificationNeeded":
        
        url = String.read(b)
        
        return PaymentVerificationNeeded(url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.url))
        
        return b.getvalue()

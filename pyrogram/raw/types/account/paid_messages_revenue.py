
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PaidMessagesRevenue(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.PaidMessagesRevenue`.

    Details:
        - Layer: ``224``
        - ID: ``1E109708``

    Parameters:
        stars_amount (``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetPaidMessagesRevenue
    """

    __slots__: List[str] = ["stars_amount"]

    ID = 0x1e109708
    QUALNAME = "types.account.PaidMessagesRevenue"

    def __init__(self, *, stars_amount: int) -> None:
        self.stars_amount = stars_amount

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaidMessagesRevenue":
        
        stars_amount = Long.read(b)
        
        return PaidMessagesRevenue(stars_amount=stars_amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.stars_amount))
        
        return b.getvalue()

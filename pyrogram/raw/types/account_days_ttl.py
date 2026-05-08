
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AccountDaysTTL(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.AccountDaysTTL`.

    Details:
        - Layer: ``224``
        - ID: ``B8D0AFDF``

    Parameters:
        days (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetAccountTTL
    """

    __slots__: List[str] = ["days"]

    ID = 0xb8d0afdf
    QUALNAME = "types.AccountDaysTTL"

    def __init__(self, *, days: int) -> None:
        self.days = days

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AccountDaysTTL":
        
        days = Int.read(b)
        
        return AccountDaysTTL(days=days)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.days))
        
        return b.getvalue()

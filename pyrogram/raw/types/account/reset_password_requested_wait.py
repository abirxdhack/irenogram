
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ResetPasswordRequestedWait(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.ResetPasswordResult`.

    Details:
        - Layer: ``224``
        - ID: ``E9EFFC7D``

    Parameters:
        until_date (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.ResetPassword
    """

    __slots__: List[str] = ["until_date"]

    ID = 0xe9effc7d
    QUALNAME = "types.account.ResetPasswordRequestedWait"

    def __init__(self, *, until_date: int) -> None:
        self.until_date = until_date

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResetPasswordRequestedWait":
        
        until_date = Int.read(b)
        
        return ResetPasswordRequestedWait(until_date=until_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.until_date))
        
        return b.getvalue()

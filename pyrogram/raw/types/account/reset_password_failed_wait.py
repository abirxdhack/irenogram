
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ResetPasswordFailedWait(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.ResetPasswordResult`.

    Details:
        - Layer: ``224``
        - ID: ``E3779861``

    Parameters:
        retry_date (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.ResetPassword
    """

    __slots__: List[str] = ["retry_date"]

    ID = 0xe3779861
    QUALNAME = "types.account.ResetPasswordFailedWait"

    def __init__(self, *, retry_date: int) -> None:
        self.retry_date = retry_date

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResetPasswordFailedWait":
        
        retry_date = Int.read(b)
        
        return ResetPasswordFailedWait(retry_date=retry_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.retry_date))
        
        return b.getvalue()

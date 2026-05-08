
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EmailVerified(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.EmailVerified`.

    Details:
        - Layer: ``224``
        - ID: ``2B96CD1B``

    Parameters:
        email (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.VerifyEmail
    """

    __slots__: List[str] = ["email"]

    ID = 0x2b96cd1b
    QUALNAME = "types.account.EmailVerified"

    def __init__(self, *, email: str) -> None:
        self.email = email

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmailVerified":
        
        email = String.read(b)
        
        return EmailVerified(email=email)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.email))
        
        return b.getvalue()

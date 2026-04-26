
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SentEmailCode(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.SentEmailCode`.

    Details:
        - Layer: ``224``
        - ID: ``811F854F``

    Parameters:
        email_pattern (``str``):
            N/A

        length (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.SendVerifyEmailCode
    """

    __slots__: List[str] = ["email_pattern", "length"]

    ID = 0x811f854f
    QUALNAME = "types.account.SentEmailCode"

    def __init__(self, *, email_pattern: str, length: int) -> None:
        self.email_pattern = email_pattern
        self.length = length

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentEmailCode":
        
        email_pattern = String.read(b)
        
        length = Int.read(b)
        
        return SentEmailCode(email_pattern=email_pattern, length=length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.email_pattern))
        
        b.write(Int(self.length))
        
        return b.getvalue()

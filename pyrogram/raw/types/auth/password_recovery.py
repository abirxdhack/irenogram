
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PasswordRecovery(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.auth.PasswordRecovery`.

    Details:
        - Layer: ``224``
        - ID: ``137948A5``

    Parameters:
        email_pattern (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.RequestPasswordRecovery
    """

    __slots__: List[str] = ["email_pattern"]

    ID = 0x137948a5
    QUALNAME = "types.auth.PasswordRecovery"

    def __init__(self, *, email_pattern: str) -> None:
        self.email_pattern = email_pattern

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PasswordRecovery":
        
        email_pattern = String.read(b)
        
        return PasswordRecovery(email_pattern=email_pattern)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.email_pattern))
        
        return b.getvalue()

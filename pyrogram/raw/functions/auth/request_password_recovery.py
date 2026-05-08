
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RequestPasswordRecovery(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D897BC66``

    Parameters:
        No parameters required.

    Returns:
        :obj:`auth.PasswordRecovery <pyrogram.raw.base.auth.PasswordRecovery>`
    """

    __slots__: List[str] = []

    ID = 0xd897bc66
    QUALNAME = "functions.auth.RequestPasswordRecovery"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestPasswordRecovery":
        
        return RequestPasswordRecovery()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

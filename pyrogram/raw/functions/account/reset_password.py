
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ResetPassword(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``9308CE1B``

    Parameters:
        No parameters required.

    Returns:
        :obj:`account.ResetPasswordResult <pyrogram.raw.base.account.ResetPasswordResult>`
    """

    __slots__: List[str] = []

    ID = 0x9308ce1b
    QUALNAME = "functions.account.ResetPassword"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResetPassword":
        
        return ResetPassword()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

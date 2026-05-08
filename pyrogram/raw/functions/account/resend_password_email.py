
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ResendPasswordEmail(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``7A7F2A15``

    Parameters:
        No parameters required.

    Returns:
        ``bool``
    """

    __slots__: List[str] = []

    ID = 0x7a7f2a15
    QUALNAME = "functions.account.ResendPasswordEmail"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResendPasswordEmail":
        
        return ResendPasswordEmail()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

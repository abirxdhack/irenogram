
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetPaidReactionPrivacy(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``472455AA``

    Parameters:
        No parameters required.

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = []

    ID = 0x472455aa
    QUALNAME = "functions.messages.GetPaidReactionPrivacy"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPaidReactionPrivacy":
        
        return GetPaidReactionPrivacy()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class IsEligibleToJoin(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``EDC39D0``

    Parameters:
        No parameters required.

    Returns:
        :obj:`smsjobs.EligibilityToJoin <pyrogram.raw.base.smsjobs.EligibilityToJoin>`
    """

    __slots__: List[str] = []

    ID = 0xedc39d0
    QUALNAME = "functions.smsjobs.IsEligibleToJoin"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "IsEligibleToJoin":
        
        return IsEligibleToJoin()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

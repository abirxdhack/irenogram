
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class Join(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A74ECE2D``

    Parameters:
        No parameters required.

    Returns:
        ``bool``
    """

    __slots__: List[str] = []

    ID = 0xa74ece2d
    QUALNAME = "functions.smsjobs.Join"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Join":
        
        return Join()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

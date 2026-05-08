
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetAllDrafts(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``6A3F8D65``

    Parameters:
        No parameters required.

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = []

    ID = 0x6a3f8d65
    QUALNAME = "functions.messages.GetAllDrafts"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAllDrafts":
        
        return GetAllDrafts()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

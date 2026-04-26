
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetNearestDc(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``1FB33026``

    Parameters:
        No parameters required.

    Returns:
        :obj:`NearestDc <pyrogram.raw.base.NearestDc>`
    """

    __slots__: List[str] = []

    ID = 0x1fb33026
    QUALNAME = "functions.help.GetNearestDc"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetNearestDc":
        
        return GetNearestDc()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

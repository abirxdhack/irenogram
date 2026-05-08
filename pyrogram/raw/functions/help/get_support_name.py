
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetSupportName(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D360E72C``

    Parameters:
        No parameters required.

    Returns:
        :obj:`help.SupportName <pyrogram.raw.base.help.SupportName>`
    """

    __slots__: List[str] = []

    ID = 0xd360e72c
    QUALNAME = "functions.help.GetSupportName"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSupportName":
        
        return GetSupportName()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

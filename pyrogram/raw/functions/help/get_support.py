
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetSupport(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``9CDF08CD``

    Parameters:
        No parameters required.

    Returns:
        :obj:`help.Support <pyrogram.raw.base.help.Support>`
    """

    __slots__: List[str] = []

    ID = 0x9cdf08cd
    QUALNAME = "functions.help.GetSupport"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSupport":
        
        return GetSupport()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

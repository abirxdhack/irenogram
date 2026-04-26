
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetAppUpdate(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``522D5A7D``

    Parameters:
        source (``str``):
            N/A

    Returns:
        :obj:`help.AppUpdate <pyrogram.raw.base.help.AppUpdate>`
    """

    __slots__: List[str] = ["source"]

    ID = 0x522d5a7d
    QUALNAME = "functions.help.GetAppUpdate"

    def __init__(self, *, source: str) -> None:
        self.source = source

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAppUpdate":
        
        source = String.read(b)
        
        return GetAppUpdate(source=source)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.source))
        
        return b.getvalue()

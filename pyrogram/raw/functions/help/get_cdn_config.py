
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetCdnConfig(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``52029342``

    Parameters:
        No parameters required.

    Returns:
        :obj:`CdnConfig <pyrogram.raw.base.CdnConfig>`
    """

    __slots__: List[str] = []

    ID = 0x52029342
    QUALNAME = "functions.help.GetCdnConfig"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetCdnConfig":
        
        return GetCdnConfig()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetMyBoosts(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``BE77B4A``

    Parameters:
        No parameters required.

    Returns:
        :obj:`premium.MyBoosts <pyrogram.raw.base.premium.MyBoosts>`
    """

    __slots__: List[str] = []

    ID = 0xbe77b4a
    QUALNAME = "functions.premium.GetMyBoosts"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMyBoosts":
        
        return GetMyBoosts()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetAdminedBots(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``B0711D83``

    Parameters:
        No parameters required.

    Returns:
        List of :obj:`User <pyrogram.raw.base.User>`
    """

    __slots__: List[str] = []

    ID = 0xb0711d83
    QUALNAME = "functions.bots.GetAdminedBots"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAdminedBots":
        
        return GetAdminedBots()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

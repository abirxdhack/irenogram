
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetBotBusinessConnection(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``76A86270``

    Parameters:
        connection_id (``str``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["connection_id"]

    ID = 0x76a86270
    QUALNAME = "functions.account.GetBotBusinessConnection"

    def __init__(self, *, connection_id: str) -> None:
        self.connection_id = connection_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBotBusinessConnection":
        
        connection_id = String.read(b)
        
        return GetBotBusinessConnection(connection_id=connection_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.connection_id))
        
        return b.getvalue()

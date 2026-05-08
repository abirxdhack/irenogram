
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetAuthorizationTTL(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``BF899AA0``

    Parameters:
        authorization_ttl_days (``int`` ``32-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["authorization_ttl_days"]

    ID = 0xbf899aa0
    QUALNAME = "functions.account.SetAuthorizationTTL"

    def __init__(self, *, authorization_ttl_days: int) -> None:
        self.authorization_ttl_days = authorization_ttl_days

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetAuthorizationTTL":
        
        authorization_ttl_days = Int.read(b)
        
        return SetAuthorizationTTL(authorization_ttl_days=authorization_ttl_days)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.authorization_ttl_days))
        
        return b.getvalue()

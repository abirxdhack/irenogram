
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetAuthorizationForm(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A929597A``

    Parameters:
        bot_id (``int`` ``64-bit``):
            N/A

        scope (``str``):
            N/A

        public_key (``str``):
            N/A

    Returns:
        :obj:`account.AuthorizationForm <pyrogram.raw.base.account.AuthorizationForm>`
    """

    __slots__: List[str] = ["bot_id", "scope", "public_key"]

    ID = 0xa929597a
    QUALNAME = "functions.account.GetAuthorizationForm"

    def __init__(self, *, bot_id: int, scope: str, public_key: str) -> None:
        self.bot_id = bot_id
        self.scope = scope
        self.public_key = public_key

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAuthorizationForm":
        
        bot_id = Long.read(b)
        
        scope = String.read(b)
        
        public_key = String.read(b)
        
        return GetAuthorizationForm(bot_id=bot_id, scope=scope, public_key=public_key)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.bot_id))
        
        b.write(String(self.scope))
        
        b.write(String(self.public_key))
        
        return b.getvalue()

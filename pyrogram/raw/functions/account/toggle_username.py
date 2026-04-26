
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ToggleUsername(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``58D6B376``

    Parameters:
        username (``str``):
            N/A

        active (``bool``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["username", "active"]

    ID = 0x58d6b376
    QUALNAME = "functions.account.ToggleUsername"

    def __init__(self, *, username: str, active: bool) -> None:
        self.username = username
        self.active = active

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleUsername":
        
        username = String.read(b)
        
        active = Bool.read(b)
        
        return ToggleUsername(username=username, active=active)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.username))
        
        b.write(Bool(self.active))
        
        return b.getvalue()

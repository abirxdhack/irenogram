
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ToggleUsername(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``53CA973``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        username (``str``):
            N/A

        active (``bool``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["bot", "username", "active"]

    ID = 0x53ca973
    QUALNAME = "functions.bots.ToggleUsername"

    def __init__(self, *, bot: "raw.base.InputUser", username: str, active: bool) -> None:
        self.bot = bot
        self.username = username
        self.active = active

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleUsername":
        
        bot = TLObject.read(b)
        
        username = String.read(b)
        
        active = Bool.read(b)
        
        return ToggleUsername(bot=bot, username=username, active=active)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.bot.write())
        
        b.write(String(self.username))
        
        b.write(Bool(self.active))
        
        return b.getvalue()

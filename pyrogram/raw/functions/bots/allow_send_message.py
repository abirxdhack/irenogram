
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AllowSendMessage(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``F132E3EF``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["bot"]

    ID = 0xf132e3ef
    QUALNAME = "functions.bots.AllowSendMessage"

    def __init__(self, *, bot: "raw.base.InputUser") -> None:
        self.bot = bot

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AllowSendMessage":
        
        bot = TLObject.read(b)
        
        return AllowSendMessage(bot=bot)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.bot.write())
        
        return b.getvalue()

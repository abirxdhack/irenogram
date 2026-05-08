
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetAttachMenuBot(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``77216192``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

    Returns:
        :obj:`AttachMenuBotsBot <pyrogram.raw.base.AttachMenuBotsBot>`
    """

    __slots__: List[str] = ["bot"]

    ID = 0x77216192
    QUALNAME = "functions.messages.GetAttachMenuBot"

    def __init__(self, *, bot: "raw.base.InputUser") -> None:
        self.bot = bot

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAttachMenuBot":
        
        bot = TLObject.read(b)
        
        return GetAttachMenuBot(bot=bot)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.bot.write())
        
        return b.getvalue()

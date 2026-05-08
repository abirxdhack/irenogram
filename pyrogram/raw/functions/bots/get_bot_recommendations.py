
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetBotRecommendations(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A1B70815``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

    Returns:
        :obj:`users.Users <pyrogram.raw.base.users.Users>`
    """

    __slots__: List[str] = ["bot"]

    ID = 0xa1b70815
    QUALNAME = "functions.bots.GetBotRecommendations"

    def __init__(self, *, bot: "raw.base.InputUser") -> None:
        self.bot = bot

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBotRecommendations":
        
        bot = TLObject.read(b)
        
        return GetBotRecommendations(bot=bot)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.bot.write())
        
        return b.getvalue()

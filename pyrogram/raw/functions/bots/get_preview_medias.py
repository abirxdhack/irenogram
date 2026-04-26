
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetPreviewMedias(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A2A5594D``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

    Returns:
        List of :obj:`BotPreviewMedia <pyrogram.raw.base.BotPreviewMedia>`
    """

    __slots__: List[str] = ["bot"]

    ID = 0xa2a5594d
    QUALNAME = "functions.bots.GetPreviewMedias"

    def __init__(self, *, bot: "raw.base.InputUser") -> None:
        self.bot = bot

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPreviewMedias":
        
        bot = TLObject.read(b)
        
        return GetPreviewMedias(bot=bot)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.bot.write())
        
        return b.getvalue()

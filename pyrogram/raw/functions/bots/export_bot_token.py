
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ExportBotToken(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``BD0D99EB``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        revoke (``bool``):
            N/A

    Returns:
        :obj:`bots.ExportedBotToken <pyrogram.raw.base.bots.ExportedBotToken>`
    """

    __slots__: List[str] = ["bot", "revoke"]

    ID = 0xbd0d99eb
    QUALNAME = "functions.bots.ExportBotToken"

    def __init__(self, *, bot: "raw.base.InputUser", revoke: bool) -> None:
        self.bot = bot
        self.revoke = revoke

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportBotToken":
        
        bot = TLObject.read(b)
        
        revoke = Bool.read(b)
        
        return ExportBotToken(bot=bot, revoke=revoke)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.bot.write())
        
        b.write(Bool(self.revoke))
        
        return b.getvalue()

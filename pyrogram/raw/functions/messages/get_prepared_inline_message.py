
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetPreparedInlineMessage(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``857EBDB8``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        id (``str``):
            N/A

    Returns:
        :obj:`messages.PreparedInlineMessage <pyrogram.raw.base.messages.PreparedInlineMessage>`
    """

    __slots__: List[str] = ["bot", "id"]

    ID = 0x857ebdb8
    QUALNAME = "functions.messages.GetPreparedInlineMessage"

    def __init__(self, *, bot: "raw.base.InputUser", id: str) -> None:
        self.bot = bot
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPreparedInlineMessage":
        
        bot = TLObject.read(b)
        
        id = String.read(b)
        
        return GetPreparedInlineMessage(bot=bot, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.bot.write())
        
        b.write(String(self.id))
        
        return b.getvalue()

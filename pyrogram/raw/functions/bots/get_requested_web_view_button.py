
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetRequestedWebViewButton(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``BF25B7F3``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        webapp_req_id (``str``):
            N/A

    Returns:
        :obj:`KeyboardButton <pyrogram.raw.base.KeyboardButton>`
    """

    __slots__: List[str] = ["bot", "webapp_req_id"]

    ID = 0xbf25b7f3
    QUALNAME = "functions.bots.GetRequestedWebViewButton"

    def __init__(self, *, bot: "raw.base.InputUser", webapp_req_id: str) -> None:
        self.bot = bot
        self.webapp_req_id = webapp_req_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetRequestedWebViewButton":
        
        bot = TLObject.read(b)
        
        webapp_req_id = String.read(b)
        
        return GetRequestedWebViewButton(bot=bot, webapp_req_id=webapp_req_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.bot.write())
        
        b.write(String(self.webapp_req_id))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InvokeWebViewCustomMethod(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``87FC5E7``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        custom_method (``str``):
            N/A

        params (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            N/A

    Returns:
        :obj:`DataJSON <pyrogram.raw.base.DataJSON>`
    """

    __slots__: List[str] = ["bot", "custom_method", "params"]

    ID = 0x87fc5e7
    QUALNAME = "functions.bots.InvokeWebViewCustomMethod"

    def __init__(self, *, bot: "raw.base.InputUser", custom_method: str, params: "raw.base.DataJSON") -> None:
        self.bot = bot
        self.custom_method = custom_method
        self.params = params

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeWebViewCustomMethod":
        
        bot = TLObject.read(b)
        
        custom_method = String.read(b)
        
        params = TLObject.read(b)
        
        return InvokeWebViewCustomMethod(bot=bot, custom_method=custom_method, params=params)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.bot.write())
        
        b.write(String(self.custom_method))
        
        b.write(self.params.write())
        
        return b.getvalue()

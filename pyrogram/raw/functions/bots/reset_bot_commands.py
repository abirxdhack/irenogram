
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ResetBotCommands(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``3D8DE0F9``

    Parameters:
        scope (:obj:`BotCommandScope <pyrogram.raw.base.BotCommandScope>`):
            N/A

        lang_code (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["scope", "lang_code"]

    ID = 0x3d8de0f9
    QUALNAME = "functions.bots.ResetBotCommands"

    def __init__(self, *, scope: "raw.base.BotCommandScope", lang_code: str) -> None:
        self.scope = scope
        self.lang_code = lang_code

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResetBotCommands":
        
        scope = TLObject.read(b)
        
        lang_code = String.read(b)
        
        return ResetBotCommands(scope=scope, lang_code=lang_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.scope.write())
        
        b.write(String(self.lang_code))
        
        return b.getvalue()

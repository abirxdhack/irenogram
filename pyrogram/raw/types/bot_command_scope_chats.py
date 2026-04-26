
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BotCommandScopeChats(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotCommandScope`.

    Details:
        - Layer: ``224``
        - ID: ``6FE1A881``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x6fe1a881
    QUALNAME = "types.BotCommandScopeChats"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotCommandScopeChats":
        
        return BotCommandScopeChats()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

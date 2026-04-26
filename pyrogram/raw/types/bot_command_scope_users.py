
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BotCommandScopeUsers(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotCommandScope`.

    Details:
        - Layer: ``224``
        - ID: ``3C4F04D8``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x3c4f04d8
    QUALNAME = "types.BotCommandScopeUsers"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotCommandScopeUsers":
        
        return BotCommandScopeUsers()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BotCommand(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotCommand`.

    Details:
        - Layer: ``224``
        - ID: ``C27AC8C7``

    Parameters:
        command (``str``):
            N/A

        description (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetBotCommands
    """

    __slots__: List[str] = ["command", "description"]

    ID = 0xc27ac8c7
    QUALNAME = "types.BotCommand"

    def __init__(self, *, command: str, description: str) -> None:
        self.command = command
        self.description = description

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotCommand":
        
        command = String.read(b)
        
        description = String.read(b)
        
        return BotCommand(command=command, description=description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.command))
        
        b.write(String(self.description))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BotInfo(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.bots.BotInfo`.

    Details:
        - Layer: ``224``
        - ID: ``E8A775B0``

    Parameters:
        name (``str``):
            N/A

        about (``str``):
            N/A

        description (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetBotInfo
    """

    __slots__: List[str] = ["name", "about", "description"]

    ID = 0xe8a775b0
    QUALNAME = "types.bots.BotInfo"

    def __init__(self, *, name: str, about: str, description: str) -> None:
        self.name = name
        self.about = about
        self.description = description

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInfo":
        
        name = String.read(b)
        
        about = String.read(b)
        
        description = String.read(b)
        
        return BotInfo(name=name, about=about, description=description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.name))
        
        b.write(String(self.about))
        
        b.write(String(self.description))
        
        return b.getvalue()

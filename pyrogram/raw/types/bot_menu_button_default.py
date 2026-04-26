
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BotMenuButtonDefault(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotMenuButton`.

    Details:
        - Layer: ``224``
        - ID: ``7533A588``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetBotMenuButton
    """

    __slots__: List[str] = []

    ID = 0x7533a588
    QUALNAME = "types.BotMenuButtonDefault"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotMenuButtonDefault":
        
        return BotMenuButtonDefault()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

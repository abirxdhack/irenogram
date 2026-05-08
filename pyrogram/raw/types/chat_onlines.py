
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChatOnlines(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatOnlines`.

    Details:
        - Layer: ``224``
        - ID: ``F041E250``

    Parameters:
        onlines (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetOnlines
    """

    __slots__: List[str] = ["onlines"]

    ID = 0xf041e250
    QUALNAME = "types.ChatOnlines"

    def __init__(self, *, onlines: int) -> None:
        self.onlines = onlines

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatOnlines":
        
        onlines = Int.read(b)
        
        return ChatOnlines(onlines=onlines)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.onlines))
        
        return b.getvalue()

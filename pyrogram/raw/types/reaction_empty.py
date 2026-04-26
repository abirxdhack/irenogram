
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReactionEmpty(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Reaction`.

    Details:
        - Layer: ``224``
        - ID: ``79F5D419``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x79f5d419
    QUALNAME = "types.ReactionEmpty"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReactionEmpty":
        
        return ReactionEmpty()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

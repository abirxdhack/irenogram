
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AvailableReactions(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.AvailableReactions`.

    Details:
        - Layer: ``224``
        - ID: ``768E3AAD``

    Parameters:
        hash (``int`` ``32-bit``):
            N/A

        reactions (List of :obj:`AvailableReaction <pyrogram.raw.base.AvailableReaction>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAvailableReactions
    """

    __slots__: List[str] = ["hash", "reactions"]

    ID = 0x768e3aad
    QUALNAME = "types.messages.AvailableReactions"

    def __init__(self, *, hash: int, reactions: List["raw.base.AvailableReaction"]) -> None:
        self.hash = hash
        self.reactions = reactions

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AvailableReactions":
        
        hash = Int.read(b)
        
        reactions = TLObject.read(b)
        
        return AvailableReactions(hash=hash, reactions=reactions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.hash))
        
        b.write(Vector(self.reactions))
        
        return b.getvalue()

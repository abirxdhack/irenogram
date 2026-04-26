
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetDefaultReaction(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``4F47A016``

    Parameters:
        reaction (:obj:`Reaction <pyrogram.raw.base.Reaction>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["reaction"]

    ID = 0x4f47a016
    QUALNAME = "functions.messages.SetDefaultReaction"

    def __init__(self, *, reaction: "raw.base.Reaction") -> None:
        self.reaction = reaction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetDefaultReaction":
        
        reaction = TLObject.read(b)
        
        return SetDefaultReaction(reaction=reaction)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.reaction.write())
        
        return b.getvalue()

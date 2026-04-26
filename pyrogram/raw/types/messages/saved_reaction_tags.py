
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SavedReactionTags(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.SavedReactionTags`.

    Details:
        - Layer: ``224``
        - ID: ``3259950A``

    Parameters:
        tags (List of :obj:`SavedReactionTag <pyrogram.raw.base.SavedReactionTag>`):
            N/A

        hash (``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSavedReactionTags
    """

    __slots__: List[str] = ["tags", "hash"]

    ID = 0x3259950a
    QUALNAME = "types.messages.SavedReactionTags"

    def __init__(self, *, tags: List["raw.base.SavedReactionTag"], hash: int) -> None:
        self.tags = tags
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedReactionTags":
        
        tags = TLObject.read(b)
        
        hash = Long.read(b)
        
        return SavedReactionTags(tags=tags, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.tags))
        
        b.write(Long(self.hash))
        
        return b.getvalue()

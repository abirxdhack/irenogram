
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SavedReactionTagsNotModified(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.SavedReactionTags`.

    Details:
        - Layer: ``224``
        - ID: ``889B59EF``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSavedReactionTags
    """

    __slots__: List[str] = []

    ID = 0x889b59ef
    QUALNAME = "types.messages.SavedReactionTagsNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedReactionTagsNotModified":
        
        return SavedReactionTagsNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

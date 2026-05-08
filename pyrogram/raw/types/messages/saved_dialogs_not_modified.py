
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SavedDialogsNotModified(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.SavedDialogs`.

    Details:
        - Layer: ``224``
        - ID: ``C01F6FE8``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSavedDialogs
            messages.GetPinnedSavedDialogs
            messages.GetSavedDialogsByID
    """

    __slots__: List[str] = ["count"]

    ID = 0xc01f6fe8
    QUALNAME = "types.messages.SavedDialogsNotModified"

    def __init__(self, *, count: int) -> None:
        self.count = count

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedDialogsNotModified":
        
        count = Int.read(b)
        
        return SavedDialogsNotModified(count=count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.count))
        
        return b.getvalue()

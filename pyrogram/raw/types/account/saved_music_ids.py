
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SavedMusicIds(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.SavedMusicIds`.

    Details:
        - Layer: ``224``
        - ID: ``998D6636``

    Parameters:
        ids (List of ``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetSavedMusicIds
    """

    __slots__: List[str] = ["ids"]

    ID = 0x998d6636
    QUALNAME = "types.account.SavedMusicIds"

    def __init__(self, *, ids: List[int]) -> None:
        self.ids = ids

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedMusicIds":
        
        ids = TLObject.read(b, Long)
        
        return SavedMusicIds(ids=ids)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.ids, Long))
        
        return b.getvalue()

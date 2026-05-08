
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SavedRingtone(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.SavedRingtone`.

    Details:
        - Layer: ``224``
        - ID: ``B7263F6D``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.SaveRingtone
    """

    __slots__: List[str] = []

    ID = 0xb7263f6d
    QUALNAME = "types.account.SavedRingtone"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedRingtone":
        
        return SavedRingtone()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

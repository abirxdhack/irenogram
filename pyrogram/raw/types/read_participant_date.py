
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReadParticipantDate(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ReadParticipantDate`.

    Details:
        - Layer: ``224``
        - ID: ``4A4FF172``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetMessageReadParticipants
    """

    __slots__: List[str] = ["user_id", "date"]

    ID = 0x4a4ff172
    QUALNAME = "types.ReadParticipantDate"

    def __init__(self, *, user_id: int, date: int) -> None:
        self.user_id = user_id
        self.date = date

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReadParticipantDate":
        
        user_id = Long.read(b)
        
        date = Int.read(b)
        
        return ReadParticipantDate(user_id=user_id, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.user_id))
        
        b.write(Int(self.date))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class HistoryImport(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.HistoryImport`.

    Details:
        - Layer: ``224``
        - ID: ``1662AF0B``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.InitHistoryImport
    """

    __slots__: List[str] = ["id"]

    ID = 0x1662af0b
    QUALNAME = "types.messages.HistoryImport"

    def __init__(self, *, id: int) -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "HistoryImport":
        
        id = Long.read(b)
        
        return HistoryImport(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DifferenceTooLong(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.updates.Difference`.

    Details:
        - Layer: ``224``
        - ID: ``4AFE8F6D``

    Parameters:
        pts (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            updates.GetDifference
    """

    __slots__: List[str] = ["pts"]

    ID = 0x4afe8f6d
    QUALNAME = "types.updates.DifferenceTooLong"

    def __init__(self, *, pts: int) -> None:
        self.pts = pts

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DifferenceTooLong":
        
        pts = Int.read(b)
        
        return DifferenceTooLong(pts=pts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.pts))
        
        return b.getvalue()

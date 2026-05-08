
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DialogsNotModified(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.Dialogs`.

    Details:
        - Layer: ``224``
        - ID: ``F0E3E596``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetDialogs
    """

    __slots__: List[str] = ["count"]

    ID = 0xf0e3e596
    QUALNAME = "types.messages.DialogsNotModified"

    def __init__(self, *, count: int) -> None:
        self.count = count

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DialogsNotModified":
        
        count = Int.read(b)
        
        return DialogsNotModified(count=count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.count))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class FavedStickersNotModified(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.FavedStickers`.

    Details:
        - Layer: ``224``
        - ID: ``9E8FA6D3``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetFavedStickers
    """

    __slots__: List[str] = []

    ID = 0x9e8fa6d3
    QUALNAME = "types.messages.FavedStickersNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FavedStickersNotModified":
        
        return FavedStickersNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

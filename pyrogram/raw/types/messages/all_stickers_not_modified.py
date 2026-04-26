
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AllStickersNotModified(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.AllStickers`.

    Details:
        - Layer: ``224``
        - ID: ``E86602C3``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAllStickers
            messages.GetMaskStickers
            messages.GetEmojiStickers
    """

    __slots__: List[str] = []

    ID = 0xe86602c3
    QUALNAME = "types.messages.AllStickersNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AllStickersNotModified":
        
        return AllStickersNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

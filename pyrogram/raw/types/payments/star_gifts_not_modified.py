
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StarGiftsNotModified(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.StarGifts`.

    Details:
        - Layer: ``224``
        - ID: ``A388A368``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarGifts
    """

    __slots__: List[str] = []

    ID = 0xa388a368
    QUALNAME = "types.payments.StarGiftsNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftsNotModified":
        
        return StarGiftsNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

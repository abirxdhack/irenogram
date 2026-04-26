
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StarGiftCollectionsNotModified(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.StarGiftCollections`.

    Details:
        - Layer: ``224``
        - ID: ``A0BA4F17``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarGiftCollections
    """

    __slots__: List[str] = []

    ID = 0xa0ba4f17
    QUALNAME = "types.payments.StarGiftCollectionsNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftCollectionsNotModified":
        
        return StarGiftCollectionsNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

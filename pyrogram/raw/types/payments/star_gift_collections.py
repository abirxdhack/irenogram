
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StarGiftCollections(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.StarGiftCollections`.

    Details:
        - Layer: ``224``
        - ID: ``8A2932F3``

    Parameters:
        collections (List of :obj:`StarGiftCollection <pyrogram.raw.base.StarGiftCollection>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarGiftCollections
    """

    __slots__: List[str] = ["collections"]

    ID = 0x8a2932f3
    QUALNAME = "types.payments.StarGiftCollections"

    def __init__(self, *, collections: List["raw.base.StarGiftCollection"]) -> None:
        self.collections = collections

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftCollections":
        
        collections = TLObject.read(b)
        
        return StarGiftCollections(collections=collections)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.collections))
        
        return b.getvalue()

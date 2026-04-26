
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AllStickers(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.AllStickers`.

    Details:
        - Layer: ``224``
        - ID: ``CDBBCEBB``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        sets (List of :obj:`StickerSet <pyrogram.raw.base.StickerSet>`):
            N/A

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAllStickers
            messages.GetMaskStickers
            messages.GetEmojiStickers
    """

    __slots__: List[str] = ["hash", "sets"]

    ID = 0xcdbbcebb
    QUALNAME = "types.messages.AllStickers"

    def __init__(self, *, hash: int, sets: List["raw.base.StickerSet"]) -> None:
        self.hash = hash
        self.sets = sets

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AllStickers":
        
        hash = Long.read(b)
        
        sets = TLObject.read(b)
        
        return AllStickers(hash=hash, sets=sets)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        b.write(Vector(self.sets))
        
        return b.getvalue()

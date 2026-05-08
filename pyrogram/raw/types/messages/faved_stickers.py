
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class FavedStickers(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.FavedStickers`.

    Details:
        - Layer: ``224``
        - ID: ``2CB51097``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        packs (List of :obj:`StickerPack <pyrogram.raw.base.StickerPack>`):
            N/A

        stickers (List of :obj:`Document <pyrogram.raw.base.Document>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetFavedStickers
    """

    __slots__: List[str] = ["hash", "packs", "stickers"]

    ID = 0x2cb51097
    QUALNAME = "types.messages.FavedStickers"

    def __init__(self, *, hash: int, packs: List["raw.base.StickerPack"], stickers: List["raw.base.Document"]) -> None:
        self.hash = hash
        self.packs = packs
        self.stickers = stickers

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FavedStickers":
        
        hash = Long.read(b)
        
        packs = TLObject.read(b)
        
        stickers = TLObject.read(b)
        
        return FavedStickers(hash=hash, packs=packs, stickers=stickers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        b.write(Vector(self.packs))
        
        b.write(Vector(self.stickers))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StickerSetFullCovered(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StickerSetCovered`.

    Details:
        - Layer: ``224``
        - ID: ``40D13C0E``

    Parameters:
        set (:obj:`StickerSet <pyrogram.raw.base.StickerSet>`):
            N/A

        packs (List of :obj:`StickerPack <pyrogram.raw.base.StickerPack>`):
            N/A

        keywords (List of :obj:`StickerKeyword <pyrogram.raw.base.StickerKeyword>`):
            N/A

        documents (List of :obj:`Document <pyrogram.raw.base.Document>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAttachedStickers
    """

    __slots__: List[str] = ["set", "packs", "keywords", "documents"]

    ID = 0x40d13c0e
    QUALNAME = "types.StickerSetFullCovered"

    def __init__(self, *, set: "raw.base.StickerSet", packs: List["raw.base.StickerPack"], keywords: List["raw.base.StickerKeyword"], documents: List["raw.base.Document"]) -> None:
        self.set = set
        self.packs = packs
        self.keywords = keywords
        self.documents = documents

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StickerSetFullCovered":
        
        set = TLObject.read(b)
        
        packs = TLObject.read(b)
        
        keywords = TLObject.read(b)
        
        documents = TLObject.read(b)
        
        return StickerSetFullCovered(set=set, packs=packs, keywords=keywords, documents=documents)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.set.write())
        
        b.write(Vector(self.packs))
        
        b.write(Vector(self.keywords))
        
        b.write(Vector(self.documents))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StarGiftAttributePattern(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAttribute`.

    Details:
        - Layer: ``224``
        - ID: ``4E7085EA``

    Parameters:
        name (``str``):
            N/A

        document (:obj:`Document <pyrogram.raw.base.Document>`):
            N/A

        rarity (:obj:`StarGiftAttributeRarity <pyrogram.raw.base.StarGiftAttributeRarity>`):
            N/A

    """

    __slots__: List[str] = ["name", "document", "rarity"]

    ID = 0x4e7085ea
    QUALNAME = "types.StarGiftAttributePattern"

    def __init__(self, *, name: str, document: "raw.base.Document", rarity: "raw.base.StarGiftAttributeRarity") -> None:
        self.name = name
        self.document = document
        self.rarity = rarity

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAttributePattern":
        
        name = String.read(b)
        
        document = TLObject.read(b)
        
        rarity = TLObject.read(b)
        
        return StarGiftAttributePattern(name=name, document=document, rarity=rarity)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.name))
        
        b.write(self.document.write())
        
        b.write(self.rarity.write())
        
        return b.getvalue()

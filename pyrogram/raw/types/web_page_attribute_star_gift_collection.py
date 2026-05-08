
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class WebPageAttributeStarGiftCollection(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.WebPageAttribute`.

    Details:
        - Layer: ``224``
        - ID: ``31CAD303``

    Parameters:
        icons (List of :obj:`Document <pyrogram.raw.base.Document>`):
            N/A

    """

    __slots__: List[str] = ["icons"]

    ID = 0x31cad303
    QUALNAME = "types.WebPageAttributeStarGiftCollection"

    def __init__(self, *, icons: List["raw.base.Document"]) -> None:
        self.icons = icons

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageAttributeStarGiftCollection":
        
        icons = TLObject.read(b)
        
        return WebPageAttributeStarGiftCollection(icons=icons)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.icons))
        
        return b.getvalue()

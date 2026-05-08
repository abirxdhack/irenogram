
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PageBlockPreformatted(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``C070D93E``

    Parameters:
        text (:obj:`RichText <pyrogram.raw.base.RichText>`):
            N/A

        language (``str``):
            N/A

    """

    __slots__: List[str] = ["text", "language"]

    ID = 0xc070d93e
    QUALNAME = "types.PageBlockPreformatted"

    def __init__(self, *, text: "raw.base.RichText", language: str) -> None:
        self.text = text
        self.language = language

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockPreformatted":
        
        text = TLObject.read(b)
        
        language = String.read(b)
        
        return PageBlockPreformatted(text=text, language=language)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.text.write())
        
        b.write(String(self.language))
        
        return b.getvalue()

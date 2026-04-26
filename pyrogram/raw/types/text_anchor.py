
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class TextAnchor(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.RichText`.

    Details:
        - Layer: ``224``
        - ID: ``35553762``

    Parameters:
        text (:obj:`RichText <pyrogram.raw.base.RichText>`):
            N/A

        name (``str``):
            N/A

    """

    __slots__: List[str] = ["text", "name"]

    ID = 0x35553762
    QUALNAME = "types.TextAnchor"

    def __init__(self, *, text: "raw.base.RichText", name: str) -> None:
        self.text = text
        self.name = name

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TextAnchor":
        
        text = TLObject.read(b)
        
        name = String.read(b)
        
        return TextAnchor(text=text, name=name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.text.write())
        
        b.write(String(self.name))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class TextConcat(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.RichText`.

    Details:
        - Layer: ``224``
        - ID: ``7E6260D7``

    Parameters:
        texts (List of :obj:`RichText <pyrogram.raw.base.RichText>`):
            N/A

    """

    __slots__: List[str] = ["texts"]

    ID = 0x7e6260d7
    QUALNAME = "types.TextConcat"

    def __init__(self, *, texts: List["raw.base.RichText"]) -> None:
        self.texts = texts

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TextConcat":
        
        texts = TLObject.read(b)
        
        return TextConcat(texts=texts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.texts))
        
        return b.getvalue()

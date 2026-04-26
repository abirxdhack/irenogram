
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputWebDocument(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputWebDocument`.

    Details:
        - Layer: ``224``
        - ID: ``9BED434D``

    Parameters:
        url (``str``):
            N/A

        size (``int`` ``32-bit``):
            N/A

        mime_type (``str``):
            N/A

        attributes (List of :obj:`DocumentAttribute <pyrogram.raw.base.DocumentAttribute>`):
            N/A

    """

    __slots__: List[str] = ["url", "size", "mime_type", "attributes"]

    ID = 0x9bed434d
    QUALNAME = "types.InputWebDocument"

    def __init__(self, *, url: str, size: int, mime_type: str, attributes: List["raw.base.DocumentAttribute"]) -> None:
        self.url = url
        self.size = size
        self.mime_type = mime_type
        self.attributes = attributes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputWebDocument":
        
        url = String.read(b)
        
        size = Int.read(b)
        
        mime_type = String.read(b)
        
        attributes = TLObject.read(b)
        
        return InputWebDocument(url=url, size=size, mime_type=mime_type, attributes=attributes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.url))
        
        b.write(Int(self.size))
        
        b.write(String(self.mime_type))
        
        b.write(Vector(self.attributes))
        
        return b.getvalue()

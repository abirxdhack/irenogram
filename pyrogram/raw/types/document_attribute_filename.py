
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DocumentAttributeFilename(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DocumentAttribute`.

    Details:
        - Layer: ``224``
        - ID: ``15590068``

    Parameters:
        file_name (``str``):
            N/A

    """

    __slots__: List[str] = ["file_name"]

    ID = 0x15590068
    QUALNAME = "types.DocumentAttributeFilename"

    def __init__(self, *, file_name: str) -> None:
        self.file_name = file_name

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeFilename":
        
        file_name = String.read(b)
        
        return DocumentAttributeFilename(file_name=file_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.file_name))
        
        return b.getvalue()

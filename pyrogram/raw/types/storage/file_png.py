
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class FilePng(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.storage.FileType`.

    Details:
        - Layer: ``224``
        - ID: ``A4F63C0``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xa4f63c0
    QUALNAME = "types.storage.FilePng"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FilePng":
        
        return FilePng()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

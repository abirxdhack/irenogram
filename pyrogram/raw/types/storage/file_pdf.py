
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class FilePdf(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.storage.FileType`.

    Details:
        - Layer: ``224``
        - ID: ``AE1E508D``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xae1e508d
    QUALNAME = "types.storage.FilePdf"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FilePdf":
        
        return FilePdf()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class FileGif(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.storage.FileType`.

    Details:
        - Layer: ``224``
        - ID: ``CAE1AADF``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xcae1aadf
    QUALNAME = "types.storage.FileGif"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FileGif":
        
        return FileGif()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

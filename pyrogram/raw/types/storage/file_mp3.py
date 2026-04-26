
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class FileMp3(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.storage.FileType`.

    Details:
        - Layer: ``224``
        - ID: ``528A0677``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x528a0677
    QUALNAME = "types.storage.FileMp3"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FileMp3":
        
        return FileMp3()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

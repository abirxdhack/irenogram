
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DeleteAutoSaveExceptions(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``53BC0020``

    Parameters:
        No parameters required.

    Returns:
        ``bool``
    """

    __slots__: List[str] = []

    ID = 0x53bc0020
    QUALNAME = "functions.account.DeleteAutoSaveExceptions"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteAutoSaveExceptions":
        
        return DeleteAutoSaveExceptions()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

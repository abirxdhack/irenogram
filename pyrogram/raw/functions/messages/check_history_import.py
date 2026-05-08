
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CheckHistoryImport(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``43FE19F3``

    Parameters:
        import_head (``str``):
            N/A

    Returns:
        :obj:`messages.HistoryImportParsed <pyrogram.raw.base.messages.HistoryImportParsed>`
    """

    __slots__: List[str] = ["import_head"]

    ID = 0x43fe19f3
    QUALNAME = "functions.messages.CheckHistoryImport"

    def __init__(self, *, import_head: str) -> None:
        self.import_head = import_head

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckHistoryImport":
        
        import_head = String.read(b)
        
        return CheckHistoryImport(import_head=import_head)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.import_head))
        
        return b.getvalue()

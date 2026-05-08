
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SendMessageHistoryImportAction(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SendMessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``DBDA9246``

    Parameters:
        progress (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["progress"]

    ID = 0xdbda9246
    QUALNAME = "types.SendMessageHistoryImportAction"

    def __init__(self, *, progress: int) -> None:
        self.progress = progress

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendMessageHistoryImportAction":
        
        progress = Int.read(b)
        
        return SendMessageHistoryImportAction(progress=progress)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.progress))
        
        return b.getvalue()

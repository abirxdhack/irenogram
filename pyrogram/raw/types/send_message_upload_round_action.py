
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SendMessageUploadRoundAction(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SendMessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``243E1C66``

    Parameters:
        progress (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["progress"]

    ID = 0x243e1c66
    QUALNAME = "types.SendMessageUploadRoundAction"

    def __init__(self, *, progress: int) -> None:
        self.progress = progress

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendMessageUploadRoundAction":
        
        progress = Int.read(b)
        
        return SendMessageUploadRoundAction(progress=progress)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.progress))
        
        return b.getvalue()

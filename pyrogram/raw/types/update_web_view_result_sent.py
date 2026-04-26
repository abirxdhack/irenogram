
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateWebViewResultSent(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``1592B79D``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["query_id"]

    ID = 0x1592b79d
    QUALNAME = "types.UpdateWebViewResultSent"

    def __init__(self, *, query_id: int) -> None:
        self.query_id = query_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateWebViewResultSent":
        
        query_id = Long.read(b)
        
        return UpdateWebViewResultSent(query_id=query_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.query_id))
        
        return b.getvalue()

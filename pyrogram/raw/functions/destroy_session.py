
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DestroySession(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``E7512126``

    Parameters:
        session_id (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`DestroySessionRes <pyrogram.raw.base.DestroySessionRes>`
    """

    __slots__: List[str] = ["session_id"]

    ID = 0xe7512126
    QUALNAME = "functions.DestroySession"

    def __init__(self, *, session_id: int) -> None:
        self.session_id = session_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DestroySession":
        
        session_id = Long.read(b)
        
        return DestroySession(session_id=session_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.session_id))
        
        return b.getvalue()

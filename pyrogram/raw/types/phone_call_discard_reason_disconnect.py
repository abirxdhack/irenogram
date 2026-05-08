
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PhoneCallDiscardReasonDisconnect(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PhoneCallDiscardReason`.

    Details:
        - Layer: ``224``
        - ID: ``E095C1A0``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xe095c1a0
    QUALNAME = "types.PhoneCallDiscardReasonDisconnect"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneCallDiscardReasonDisconnect":
        
        return PhoneCallDiscardReasonDisconnect()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

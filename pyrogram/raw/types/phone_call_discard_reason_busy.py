
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PhoneCallDiscardReasonBusy(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PhoneCallDiscardReason`.

    Details:
        - Layer: ``224``
        - ID: ``FAF7E8C9``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xfaf7e8c9
    QUALNAME = "types.PhoneCallDiscardReasonBusy"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneCallDiscardReasonBusy":
        
        return PhoneCallDiscardReasonBusy()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

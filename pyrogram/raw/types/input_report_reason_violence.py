
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputReportReasonViolence(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ReportReason`.

    Details:
        - Layer: ``224``
        - ID: ``1E22C78D``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x1e22c78d
    QUALNAME = "types.InputReportReasonViolence"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputReportReasonViolence":
        
        return InputReportReasonViolence()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

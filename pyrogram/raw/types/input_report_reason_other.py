
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputReportReasonOther(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ReportReason`.

    Details:
        - Layer: ``224``
        - ID: ``C1E4A2B1``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xc1e4a2b1
    QUALNAME = "types.InputReportReasonOther"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputReportReasonOther":
        
        return InputReportReasonOther()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

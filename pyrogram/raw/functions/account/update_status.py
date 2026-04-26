
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateStatus(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``6628562C``

    Parameters:
        offline (``bool``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["offline"]

    ID = 0x6628562c
    QUALNAME = "functions.account.UpdateStatus"

    def __init__(self, *, offline: bool) -> None:
        self.offline = offline

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStatus":
        
        offline = Bool.read(b)
        
        return UpdateStatus(offline=offline)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Bool(self.offline))
        
        return b.getvalue()

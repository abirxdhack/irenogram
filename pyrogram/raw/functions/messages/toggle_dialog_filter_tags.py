
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ToggleDialogFilterTags(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``FD2DDA49``

    Parameters:
        enabled (``bool``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["enabled"]

    ID = 0xfd2dda49
    QUALNAME = "functions.messages.ToggleDialogFilterTags"

    def __init__(self, *, enabled: bool) -> None:
        self.enabled = enabled

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleDialogFilterTags":
        
        enabled = Bool.read(b)
        
        return ToggleDialogFilterTags(enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Bool(self.enabled))
        
        return b.getvalue()

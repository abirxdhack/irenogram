
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputQuickReplyShortcut(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputQuickReplyShortcut`.

    Details:
        - Layer: ``224``
        - ID: ``24596D41``

    Parameters:
        shortcut (``str``):
            N/A

    """

    __slots__: List[str] = ["shortcut"]

    ID = 0x24596d41
    QUALNAME = "types.InputQuickReplyShortcut"

    def __init__(self, *, shortcut: str) -> None:
        self.shortcut = shortcut

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputQuickReplyShortcut":
        
        shortcut = String.read(b)
        
        return InputQuickReplyShortcut(shortcut=shortcut)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.shortcut))
        
        return b.getvalue()

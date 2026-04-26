
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EditQuickReplyShortcut(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``5C003CEF``

    Parameters:
        shortcut_id (``int`` ``32-bit``):
            N/A

        shortcut (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["shortcut_id", "shortcut"]

    ID = 0x5c003cef
    QUALNAME = "functions.messages.EditQuickReplyShortcut"

    def __init__(self, *, shortcut_id: int, shortcut: str) -> None:
        self.shortcut_id = shortcut_id
        self.shortcut = shortcut

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditQuickReplyShortcut":
        
        shortcut_id = Int.read(b)
        
        shortcut = String.read(b)
        
        return EditQuickReplyShortcut(shortcut_id=shortcut_id, shortcut=shortcut)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.shortcut_id))
        
        b.write(String(self.shortcut))
        
        return b.getvalue()

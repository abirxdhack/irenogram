
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ToggleAllStoriesHidden(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``7C2557C4``

    Parameters:
        hidden (``bool``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["hidden"]

    ID = 0x7c2557c4
    QUALNAME = "functions.stories.ToggleAllStoriesHidden"

    def __init__(self, *, hidden: bool) -> None:
        self.hidden = hidden

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleAllStoriesHidden":
        
        hidden = Bool.read(b)
        
        return ToggleAllStoriesHidden(hidden=hidden)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Bool(self.hidden))
        
        return b.getvalue()

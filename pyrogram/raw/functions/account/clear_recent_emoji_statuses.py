
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ClearRecentEmojiStatuses(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``18201AAE``

    Parameters:
        No parameters required.

    Returns:
        ``bool``
    """

    __slots__: List[str] = []

    ID = 0x18201aae
    QUALNAME = "functions.account.ClearRecentEmojiStatuses"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ClearRecentEmojiStatuses":
        
        return ClearRecentEmojiStatuses()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetChannelDefaultEmojiStatuses(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``7727A7D5``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`account.EmojiStatuses <pyrogram.raw.base.account.EmojiStatuses>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x7727a7d5
    QUALNAME = "functions.account.GetChannelDefaultEmojiStatuses"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChannelDefaultEmojiStatuses":
        
        hash = Long.read(b)
        
        return GetChannelDefaultEmojiStatuses(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        return b.getvalue()

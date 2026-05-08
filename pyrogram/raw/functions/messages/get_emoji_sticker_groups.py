
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetEmojiStickerGroups(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``1DD840F5``

    Parameters:
        hash (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.EmojiGroups <pyrogram.raw.base.messages.EmojiGroups>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x1dd840f5
    QUALNAME = "functions.messages.GetEmojiStickerGroups"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetEmojiStickerGroups":
        
        hash = Int.read(b)
        
        return GetEmojiStickerGroups(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.hash))
        
        return b.getvalue()

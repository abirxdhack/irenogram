
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetDefaultBackgroundEmojis(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A60AB9CE``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`EmojiList <pyrogram.raw.base.EmojiList>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0xa60ab9ce
    QUALNAME = "functions.account.GetDefaultBackgroundEmojis"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDefaultBackgroundEmojis":
        
        hash = Long.read(b)
        
        return GetDefaultBackgroundEmojis(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetChannelRestrictedStatusEmojis(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``35A9E0D5``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`EmojiList <pyrogram.raw.base.EmojiList>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x35a9e0d5
    QUALNAME = "functions.account.GetChannelRestrictedStatusEmojis"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChannelRestrictedStatusEmojis":
        
        hash = Long.read(b)
        
        return GetChannelRestrictedStatusEmojis(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        return b.getvalue()

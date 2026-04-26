
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetEmojiGameInfo(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``FB7E8CA7``

    Parameters:
        No parameters required.

    Returns:
        :obj:`messages.EmojiGameInfo <pyrogram.raw.base.messages.EmojiGameInfo>`
    """

    __slots__: List[str] = []

    ID = 0xfb7e8ca7
    QUALNAME = "functions.messages.GetEmojiGameInfo"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetEmojiGameInfo":
        
        return GetEmojiGameInfo()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

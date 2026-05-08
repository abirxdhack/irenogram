
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetEmojiKeywords(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``35A0E062``

    Parameters:
        lang_code (``str``):
            N/A

    Returns:
        :obj:`EmojiKeywordsDifference <pyrogram.raw.base.EmojiKeywordsDifference>`
    """

    __slots__: List[str] = ["lang_code"]

    ID = 0x35a0e062
    QUALNAME = "functions.messages.GetEmojiKeywords"

    def __init__(self, *, lang_code: str) -> None:
        self.lang_code = lang_code

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetEmojiKeywords":
        
        lang_code = String.read(b)
        
        return GetEmojiKeywords(lang_code=lang_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.lang_code))
        
        return b.getvalue()

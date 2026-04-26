
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EmojiGroupGreeting(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.EmojiGroup`.

    Details:
        - Layer: ``224``
        - ID: ``80D26CC7``

    Parameters:
        title (``str``):
            N/A

        icon_emoji_id (``int`` ``64-bit``):
            N/A

        emoticons (List of ``str``):
            N/A

    """

    __slots__: List[str] = ["title", "icon_emoji_id", "emoticons"]

    ID = 0x80d26cc7
    QUALNAME = "types.EmojiGroupGreeting"

    def __init__(self, *, title: str, icon_emoji_id: int, emoticons: List[str]) -> None:
        self.title = title
        self.icon_emoji_id = icon_emoji_id
        self.emoticons = emoticons

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiGroupGreeting":
        
        title = String.read(b)
        
        icon_emoji_id = Long.read(b)
        
        emoticons = TLObject.read(b, String)
        
        return EmojiGroupGreeting(title=title, icon_emoji_id=icon_emoji_id, emoticons=emoticons)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.title))
        
        b.write(Long(self.icon_emoji_id))
        
        b.write(Vector(self.emoticons, String))
        
        return b.getvalue()

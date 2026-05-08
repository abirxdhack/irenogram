
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateUserEmojiStatus(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``ED9F30C5``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        emoji_status (:obj:`EmojiStatus <pyrogram.raw.base.EmojiStatus>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["user_id", "emoji_status"]

    ID = 0xed9f30c5
    QUALNAME = "functions.bots.UpdateUserEmojiStatus"

    def __init__(self, *, user_id: "raw.base.InputUser", emoji_status: "raw.base.EmojiStatus") -> None:
        self.user_id = user_id
        self.emoji_status = emoji_status

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateUserEmojiStatus":
        
        user_id = TLObject.read(b)
        
        emoji_status = TLObject.read(b)
        
        return UpdateUserEmojiStatus(user_id=user_id, emoji_status=emoji_status)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.user_id.write())
        
        b.write(self.emoji_status.write())
        
        return b.getvalue()

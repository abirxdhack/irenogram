
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SendMessageEmojiInteractionSeen(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SendMessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``B665902E``

    Parameters:
        emoticon (``str``):
            N/A

    """

    __slots__: List[str] = ["emoticon"]

    ID = 0xb665902e
    QUALNAME = "types.SendMessageEmojiInteractionSeen"

    def __init__(self, *, emoticon: str) -> None:
        self.emoticon = emoticon

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendMessageEmojiInteractionSeen":
        
        emoticon = String.read(b)
        
        return SendMessageEmojiInteractionSeen(emoticon=emoticon)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.emoticon))
        
        return b.getvalue()

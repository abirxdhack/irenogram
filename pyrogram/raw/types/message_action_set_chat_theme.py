
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageActionSetChatTheme(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``B91BBD3A``

    Parameters:
        theme (:obj:`ChatTheme <pyrogram.raw.base.ChatTheme>`):
            N/A

    """

    __slots__: List[str] = ["theme"]

    ID = 0xb91bbd3a
    QUALNAME = "types.MessageActionSetChatTheme"

    def __init__(self, *, theme: "raw.base.ChatTheme") -> None:
        self.theme = theme

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSetChatTheme":
        
        theme = TLObject.read(b)
        
        return MessageActionSetChatTheme(theme=theme)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.theme.write())
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageActionWebViewDataSentMe(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``47DD8079``

    Parameters:
        text (``str``):
            N/A

        data (``str``):
            N/A

    """

    __slots__: List[str] = ["text", "data"]

    ID = 0x47dd8079
    QUALNAME = "types.MessageActionWebViewDataSentMe"

    def __init__(self, *, text: str, data: str) -> None:
        self.text = text
        self.data = data

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionWebViewDataSentMe":
        
        text = String.read(b)
        
        data = String.read(b)
        
        return MessageActionWebViewDataSentMe(text=text, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.text))
        
        b.write(String(self.data))
        
        return b.getvalue()

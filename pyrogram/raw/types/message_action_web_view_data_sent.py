
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageActionWebViewDataSent(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``B4C38CB5``

    Parameters:
        text (``str``):
            N/A

    """

    __slots__: List[str] = ["text"]

    ID = 0xb4c38cb5
    QUALNAME = "types.MessageActionWebViewDataSent"

    def __init__(self, *, text: str) -> None:
        self.text = text

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionWebViewDataSent":
        
        text = String.read(b)
        
        return MessageActionWebViewDataSent(text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.text))
        
        return b.getvalue()

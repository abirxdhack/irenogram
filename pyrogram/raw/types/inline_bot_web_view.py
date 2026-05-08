
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InlineBotWebView(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InlineBotWebView`.

    Details:
        - Layer: ``224``
        - ID: ``B57295D5``

    Parameters:
        text (``str``):
            N/A

        url (``str``):
            N/A

    """

    __slots__: List[str] = ["text", "url"]

    ID = 0xb57295d5
    QUALNAME = "types.InlineBotWebView"

    def __init__(self, *, text: str, url: str) -> None:
        self.text = text
        self.url = url

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InlineBotWebView":
        
        text = String.read(b)
        
        url = String.read(b)
        
        return InlineBotWebView(text=text, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.text))
        
        b.write(String(self.url))
        
        return b.getvalue()

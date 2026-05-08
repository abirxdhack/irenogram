
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class KeyboardButtonSimpleWebView(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``224``
        - ID: ``E15C4370``

    Parameters:
        text (``str``):
            N/A

        url (``str``):
            N/A

        style (:obj:`KeyboardButtonStyle <pyrogram.raw.base.KeyboardButtonStyle>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetRequestedWebViewButton
    """

    __slots__: List[str] = ["text", "url", "style"]

    ID = 0xe15c4370
    QUALNAME = "types.KeyboardButtonSimpleWebView"

    def __init__(self, *, text: str, url: str, style: "raw.base.KeyboardButtonStyle" = None) -> None:
        self.text = text
        self.url = url
        self.style = style

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonSimpleWebView":
        
        flags = Int.read(b)
        
        style = TLObject.read(b) if flags & (1 << 10) else None
        
        text = String.read(b)
        
        url = String.read(b)
        
        return KeyboardButtonSimpleWebView(text=text, url=url, style=style)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 10) if self.style is not None else 0
        b.write(Int(flags))
        
        if self.style is not None:
            b.write(self.style.write())
        
        b.write(String(self.text))
        
        b.write(String(self.url))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class KeyboardButtonUrlAuth(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``224``
        - ID: ``F51006F9``

    Parameters:
        text (``str``):
            N/A

        url (``str``):
            N/A

        button_id (``int`` ``32-bit``):
            N/A

        style (:obj:`KeyboardButtonStyle <pyrogram.raw.base.KeyboardButtonStyle>`, *optional*):
            N/A

        fwd_text (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetRequestedWebViewButton
    """

    __slots__: List[str] = ["text", "url", "button_id", "style", "fwd_text"]

    ID = 0xf51006f9
    QUALNAME = "types.KeyboardButtonUrlAuth"

    def __init__(self, *, text: str, url: str, button_id: int, style: "raw.base.KeyboardButtonStyle" = None, fwd_text: Optional[str] = None) -> None:
        self.text = text
        self.url = url
        self.button_id = button_id
        self.style = style
        self.fwd_text = fwd_text

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonUrlAuth":
        
        flags = Int.read(b)
        
        style = TLObject.read(b) if flags & (1 << 10) else None
        
        text = String.read(b)
        
        fwd_text = String.read(b) if flags & (1 << 0) else None
        url = String.read(b)
        
        button_id = Int.read(b)
        
        return KeyboardButtonUrlAuth(text=text, url=url, button_id=button_id, style=style, fwd_text=fwd_text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 10) if self.style is not None else 0
        flags |= (1 << 0) if self.fwd_text is not None else 0
        b.write(Int(flags))
        
        if self.style is not None:
            b.write(self.style.write())
        
        b.write(String(self.text))
        
        if self.fwd_text is not None:
            b.write(String(self.fwd_text))
        
        b.write(String(self.url))
        
        b.write(Int(self.button_id))
        
        return b.getvalue()

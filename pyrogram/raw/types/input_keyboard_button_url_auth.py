
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputKeyboardButtonUrlAuth(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``224``
        - ID: ``68013E72``

    Parameters:
        text (``str``):
            N/A

        url (``str``):
            N/A

        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        request_write_access (``bool``, *optional*):
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

    __slots__: List[str] = ["text", "url", "bot", "request_write_access", "style", "fwd_text"]

    ID = 0x68013e72
    QUALNAME = "types.InputKeyboardButtonUrlAuth"

    def __init__(self, *, text: str, url: str, bot: "raw.base.InputUser", request_write_access: Optional[bool] = None, style: "raw.base.KeyboardButtonStyle" = None, fwd_text: Optional[str] = None) -> None:
        self.text = text
        self.url = url
        self.bot = bot
        self.request_write_access = request_write_access
        self.style = style
        self.fwd_text = fwd_text

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputKeyboardButtonUrlAuth":
        
        flags = Int.read(b)
        
        request_write_access = True if flags & (1 << 0) else False
        style = TLObject.read(b) if flags & (1 << 10) else None
        
        text = String.read(b)
        
        fwd_text = String.read(b) if flags & (1 << 1) else None
        url = String.read(b)
        
        bot = TLObject.read(b)
        
        return InputKeyboardButtonUrlAuth(text=text, url=url, bot=bot, request_write_access=request_write_access, style=style, fwd_text=fwd_text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.request_write_access else 0
        flags |= (1 << 10) if self.style is not None else 0
        flags |= (1 << 1) if self.fwd_text is not None else 0
        b.write(Int(flags))
        
        if self.style is not None:
            b.write(self.style.write())
        
        b.write(String(self.text))
        
        if self.fwd_text is not None:
            b.write(String(self.fwd_text))
        
        b.write(String(self.url))
        
        b.write(self.bot.write())
        
        return b.getvalue()

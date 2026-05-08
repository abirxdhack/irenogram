
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputKeyboardButtonUserProfile(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``224``
        - ID: ``7D5E07C7``

    Parameters:
        text (``str``):
            N/A

        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
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

    __slots__: List[str] = ["text", "user_id", "style"]

    ID = 0x7d5e07c7
    QUALNAME = "types.InputKeyboardButtonUserProfile"

    def __init__(self, *, text: str, user_id: "raw.base.InputUser", style: "raw.base.KeyboardButtonStyle" = None) -> None:
        self.text = text
        self.user_id = user_id
        self.style = style

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputKeyboardButtonUserProfile":
        
        flags = Int.read(b)
        
        style = TLObject.read(b) if flags & (1 << 10) else None
        
        text = String.read(b)
        
        user_id = TLObject.read(b)
        
        return InputKeyboardButtonUserProfile(text=text, user_id=user_id, style=style)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 10) if self.style is not None else 0
        b.write(Int(flags))
        
        if self.style is not None:
            b.write(self.style.write())
        
        b.write(String(self.text))
        
        b.write(self.user_id.write())
        
        return b.getvalue()

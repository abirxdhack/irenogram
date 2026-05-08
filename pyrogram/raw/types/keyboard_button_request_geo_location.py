
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class KeyboardButtonRequestGeoLocation(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``224``
        - ID: ``AA40F94D``

    Parameters:
        text (``str``):
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

    __slots__: List[str] = ["text", "style"]

    ID = 0xaa40f94d
    QUALNAME = "types.KeyboardButtonRequestGeoLocation"

    def __init__(self, *, text: str, style: "raw.base.KeyboardButtonStyle" = None) -> None:
        self.text = text
        self.style = style

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonRequestGeoLocation":
        
        flags = Int.read(b)
        
        style = TLObject.read(b) if flags & (1 << 10) else None
        
        text = String.read(b)
        
        return KeyboardButtonRequestGeoLocation(text=text, style=style)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 10) if self.style is not None else 0
        b.write(Int(flags))
        
        if self.style is not None:
            b.write(self.style.write())
        
        b.write(String(self.text))
        
        return b.getvalue()

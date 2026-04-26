
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateTheme(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``8216FBA3``

    Parameters:
        theme (:obj:`Theme <pyrogram.raw.base.Theme>`):
            N/A

    """

    __slots__: List[str] = ["theme"]

    ID = 0x8216fba3
    QUALNAME = "types.UpdateTheme"

    def __init__(self, *, theme: "raw.base.Theme") -> None:
        self.theme = theme

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateTheme":
        
        theme = TLObject.read(b)
        
        return UpdateTheme(theme=theme)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.theme.write())
        
        return b.getvalue()

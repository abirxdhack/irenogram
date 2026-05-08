
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class KeyboardButtonRow(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButtonRow`.

    Details:
        - Layer: ``224``
        - ID: ``77608B83``

    Parameters:
        buttons (List of :obj:`KeyboardButton <pyrogram.raw.base.KeyboardButton>`):
            N/A

    """

    __slots__: List[str] = ["buttons"]

    ID = 0x77608b83
    QUALNAME = "types.KeyboardButtonRow"

    def __init__(self, *, buttons: List["raw.base.KeyboardButton"]) -> None:
        self.buttons = buttons

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonRow":
        
        buttons = TLObject.read(b)
        
        return KeyboardButtonRow(buttons=buttons)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.buttons))
        
        return b.getvalue()

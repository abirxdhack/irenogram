
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReplyKeyboardHide(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ReplyMarkup`.

    Details:
        - Layer: ``224``
        - ID: ``A03E5B85``

    Parameters:
        selective (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["selective"]

    ID = 0xa03e5b85
    QUALNAME = "types.ReplyKeyboardHide"

    def __init__(self, *, selective: Optional[bool] = None) -> None:
        self.selective = selective

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReplyKeyboardHide":
        
        flags = Int.read(b)
        
        selective = True if flags & (1 << 2) else False
        return ReplyKeyboardHide(selective=selective)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.selective else 0
        b.write(Int(flags))
        
        return b.getvalue()

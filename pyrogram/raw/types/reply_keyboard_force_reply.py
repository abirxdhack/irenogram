
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReplyKeyboardForceReply(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ReplyMarkup`.

    Details:
        - Layer: ``224``
        - ID: ``86B40B08``

    Parameters:
        single_use (``bool``, *optional*):
            N/A

        selective (``bool``, *optional*):
            N/A

        placeholder (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["single_use", "selective", "placeholder"]

    ID = 0x86b40b08
    QUALNAME = "types.ReplyKeyboardForceReply"

    def __init__(self, *, single_use: Optional[bool] = None, selective: Optional[bool] = None, placeholder: Optional[str] = None) -> None:
        self.single_use = single_use
        self.selective = selective
        self.placeholder = placeholder

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReplyKeyboardForceReply":
        
        flags = Int.read(b)
        
        single_use = True if flags & (1 << 1) else False
        selective = True if flags & (1 << 2) else False
        placeholder = String.read(b) if flags & (1 << 3) else None
        return ReplyKeyboardForceReply(single_use=single_use, selective=selective, placeholder=placeholder)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.single_use else 0
        flags |= (1 << 2) if self.selective else 0
        flags |= (1 << 3) if self.placeholder is not None else 0
        b.write(Int(flags))
        
        if self.placeholder is not None:
            b.write(String(self.placeholder))
        
        return b.getvalue()

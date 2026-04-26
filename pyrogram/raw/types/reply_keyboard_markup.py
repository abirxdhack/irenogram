
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReplyKeyboardMarkup(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ReplyMarkup`.

    Details:
        - Layer: ``224``
        - ID: ``85DD99D1``

    Parameters:
        rows (List of :obj:`KeyboardButtonRow <pyrogram.raw.base.KeyboardButtonRow>`):
            N/A

        resize (``bool``, *optional*):
            N/A

        single_use (``bool``, *optional*):
            N/A

        selective (``bool``, *optional*):
            N/A

        persistent (``bool``, *optional*):
            N/A

        placeholder (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["rows", "resize", "single_use", "selective", "persistent", "placeholder"]

    ID = 0x85dd99d1
    QUALNAME = "types.ReplyKeyboardMarkup"

    def __init__(self, *, rows: List["raw.base.KeyboardButtonRow"], resize: Optional[bool] = None, single_use: Optional[bool] = None, selective: Optional[bool] = None, persistent: Optional[bool] = None, placeholder: Optional[str] = None) -> None:
        self.rows = rows
        self.resize = resize
        self.single_use = single_use
        self.selective = selective
        self.persistent = persistent
        self.placeholder = placeholder

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReplyKeyboardMarkup":
        
        flags = Int.read(b)
        
        resize = True if flags & (1 << 0) else False
        single_use = True if flags & (1 << 1) else False
        selective = True if flags & (1 << 2) else False
        persistent = True if flags & (1 << 4) else False
        rows = TLObject.read(b)
        
        placeholder = String.read(b) if flags & (1 << 3) else None
        return ReplyKeyboardMarkup(rows=rows, resize=resize, single_use=single_use, selective=selective, persistent=persistent, placeholder=placeholder)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.resize else 0
        flags |= (1 << 1) if self.single_use else 0
        flags |= (1 << 2) if self.selective else 0
        flags |= (1 << 4) if self.persistent else 0
        flags |= (1 << 3) if self.placeholder is not None else 0
        b.write(Int(flags))
        
        b.write(Vector(self.rows))
        
        if self.placeholder is not None:
            b.write(String(self.placeholder))
        
        return b.getvalue()

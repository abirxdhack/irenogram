
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PageBlockOrderedList(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``9A8AE1E1``

    Parameters:
        items (List of :obj:`PageListOrderedItem <pyrogram.raw.base.PageListOrderedItem>`):
            N/A

    """

    __slots__: List[str] = ["items"]

    ID = 0x9a8ae1e1
    QUALNAME = "types.PageBlockOrderedList"

    def __init__(self, *, items: List["raw.base.PageListOrderedItem"]) -> None:
        self.items = items

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockOrderedList":
        
        items = TLObject.read(b)
        
        return PageBlockOrderedList(items=items)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.items))
        
        return b.getvalue()

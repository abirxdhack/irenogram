
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PageListItemBlocks(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageListItem`.

    Details:
        - Layer: ``224``
        - ID: ``25E073FC``

    Parameters:
        blocks (List of :obj:`PageBlock <pyrogram.raw.base.PageBlock>`):
            N/A

    """

    __slots__: List[str] = ["blocks"]

    ID = 0x25e073fc
    QUALNAME = "types.PageListItemBlocks"

    def __init__(self, *, blocks: List["raw.base.PageBlock"]) -> None:
        self.blocks = blocks

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageListItemBlocks":
        
        blocks = TLObject.read(b)
        
        return PageListItemBlocks(blocks=blocks)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.blocks))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PageTableRow(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageTableRow`.

    Details:
        - Layer: ``224``
        - ID: ``E0C0C5E5``

    Parameters:
        cells (List of :obj:`PageTableCell <pyrogram.raw.base.PageTableCell>`):
            N/A

    """

    __slots__: List[str] = ["cells"]

    ID = 0xe0c0c5e5
    QUALNAME = "types.PageTableRow"

    def __init__(self, *, cells: List["raw.base.PageTableCell"]) -> None:
        self.cells = cells

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageTableRow":
        
        cells = TLObject.read(b)
        
        return PageTableRow(cells=cells)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.cells))
        
        return b.getvalue()

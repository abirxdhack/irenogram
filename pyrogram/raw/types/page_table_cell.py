
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PageTableCell(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageTableCell`.

    Details:
        - Layer: ``224``
        - ID: ``34566B6A``

    Parameters:
        header (``bool``, *optional*):
            N/A

        align_center (``bool``, *optional*):
            N/A

        align_right (``bool``, *optional*):
            N/A

        valign_middle (``bool``, *optional*):
            N/A

        valign_bottom (``bool``, *optional*):
            N/A

        text (:obj:`RichText <pyrogram.raw.base.RichText>`, *optional*):
            N/A

        colspan (``int`` ``32-bit``, *optional*):
            N/A

        rowspan (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["header", "align_center", "align_right", "valign_middle", "valign_bottom", "text", "colspan", "rowspan"]

    ID = 0x34566b6a
    QUALNAME = "types.PageTableCell"

    def __init__(self, *, header: Optional[bool] = None, align_center: Optional[bool] = None, align_right: Optional[bool] = None, valign_middle: Optional[bool] = None, valign_bottom: Optional[bool] = None, text: "raw.base.RichText" = None, colspan: Optional[int] = None, rowspan: Optional[int] = None) -> None:
        self.header = header
        self.align_center = align_center
        self.align_right = align_right
        self.valign_middle = valign_middle
        self.valign_bottom = valign_bottom
        self.text = text
        self.colspan = colspan
        self.rowspan = rowspan

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageTableCell":
        
        flags = Int.read(b)
        
        header = True if flags & (1 << 0) else False
        align_center = True if flags & (1 << 3) else False
        align_right = True if flags & (1 << 4) else False
        valign_middle = True if flags & (1 << 5) else False
        valign_bottom = True if flags & (1 << 6) else False
        text = TLObject.read(b) if flags & (1 << 7) else None
        
        colspan = Int.read(b) if flags & (1 << 1) else None
        rowspan = Int.read(b) if flags & (1 << 2) else None
        return PageTableCell(header=header, align_center=align_center, align_right=align_right, valign_middle=valign_middle, valign_bottom=valign_bottom, text=text, colspan=colspan, rowspan=rowspan)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.header else 0
        flags |= (1 << 3) if self.align_center else 0
        flags |= (1 << 4) if self.align_right else 0
        flags |= (1 << 5) if self.valign_middle else 0
        flags |= (1 << 6) if self.valign_bottom else 0
        flags |= (1 << 7) if self.text is not None else 0
        flags |= (1 << 1) if self.colspan is not None else 0
        flags |= (1 << 2) if self.rowspan is not None else 0
        b.write(Int(flags))
        
        if self.text is not None:
            b.write(self.text.write())
        
        if self.colspan is not None:
            b.write(Int(self.colspan))
        
        if self.rowspan is not None:
            b.write(Int(self.rowspan))
        
        return b.getvalue()

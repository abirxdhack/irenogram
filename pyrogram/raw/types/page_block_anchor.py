
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PageBlockAnchor(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``CE0D37B0``

    Parameters:
        name (``str``):
            N/A

    """

    __slots__: List[str] = ["name"]

    ID = 0xce0d37b0
    QUALNAME = "types.PageBlockAnchor"

    def __init__(self, *, name: str) -> None:
        self.name = name

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockAnchor":
        
        name = String.read(b)
        
        return PageBlockAnchor(name=name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.name))
        
        return b.getvalue()

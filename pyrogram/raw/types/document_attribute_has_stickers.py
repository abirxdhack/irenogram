
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DocumentAttributeHasStickers(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DocumentAttribute`.

    Details:
        - Layer: ``224``
        - ID: ``9801D2F7``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x9801d2f7
    QUALNAME = "types.DocumentAttributeHasStickers"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeHasStickers":
        
        return DocumentAttributeHasStickers()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

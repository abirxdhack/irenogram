
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DocumentAttributeAnimated(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DocumentAttribute`.

    Details:
        - Layer: ``224``
        - ID: ``11B58939``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x11b58939
    QUALNAME = "types.DocumentAttributeAnimated"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeAnimated":
        
        return DocumentAttributeAnimated()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

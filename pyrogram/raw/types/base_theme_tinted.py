
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BaseThemeTinted(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BaseTheme`.

    Details:
        - Layer: ``224``
        - ID: ``6D5F77EE``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x6d5f77ee
    QUALNAME = "types.BaseThemeTinted"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BaseThemeTinted":
        
        return BaseThemeTinted()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

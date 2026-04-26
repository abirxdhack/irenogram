
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BaseThemeClassic(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BaseTheme`.

    Details:
        - Layer: ``224``
        - ID: ``C3A12462``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xc3a12462
    QUALNAME = "types.BaseThemeClassic"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BaseThemeClassic":
        
        return BaseThemeClassic()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputUserSelf(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputUser`.

    Details:
        - Layer: ``224``
        - ID: ``F7C1B13F``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xf7c1b13f
    QUALNAME = "types.InputUserSelf"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputUserSelf":
        
        return InputUserSelf()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

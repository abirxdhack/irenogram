
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CodeTypeCall(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.auth.CodeType`.

    Details:
        - Layer: ``224``
        - ID: ``741CD3E3``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x741cd3e3
    QUALNAME = "types.auth.CodeTypeCall"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CodeTypeCall":
        
        return CodeTypeCall()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

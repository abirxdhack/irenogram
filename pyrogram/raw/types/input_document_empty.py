
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputDocumentEmpty(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputDocument`.

    Details:
        - Layer: ``224``
        - ID: ``72F0EAAE``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x72f0eaae
    QUALNAME = "types.InputDocumentEmpty"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputDocumentEmpty":
        
        return InputDocumentEmpty()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

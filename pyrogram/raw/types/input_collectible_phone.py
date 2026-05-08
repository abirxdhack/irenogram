
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputCollectiblePhone(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputCollectible`.

    Details:
        - Layer: ``224``
        - ID: ``A2E214A4``

    Parameters:
        phone (``str``):
            N/A

    """

    __slots__: List[str] = ["phone"]

    ID = 0xa2e214a4
    QUALNAME = "types.InputCollectiblePhone"

    def __init__(self, *, phone: str) -> None:
        self.phone = phone

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputCollectiblePhone":
        
        phone = String.read(b)
        
        return InputCollectiblePhone(phone=phone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.phone))
        
        return b.getvalue()

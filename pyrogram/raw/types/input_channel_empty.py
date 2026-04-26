
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputChannelEmpty(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputChannel`.

    Details:
        - Layer: ``224``
        - ID: ``EE8C1E86``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xee8c1e86
    QUALNAME = "types.InputChannelEmpty"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputChannelEmpty":
        
        return InputChannelEmpty()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

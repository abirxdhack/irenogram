
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMessagesFilterVideo(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessagesFilter`.

    Details:
        - Layer: ``224``
        - ID: ``9FC00E65``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x9fc00e65
    QUALNAME = "types.InputMessagesFilterVideo"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMessagesFilterVideo":
        
        return InputMessagesFilterVideo()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

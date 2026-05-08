
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputChatThemeEmpty(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputChatTheme`.

    Details:
        - Layer: ``224``
        - ID: ``83268483``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x83268483
    QUALNAME = "types.InputChatThemeEmpty"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputChatThemeEmpty":
        
        return InputChatThemeEmpty()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

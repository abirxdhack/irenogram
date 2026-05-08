
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMessagesFilterPhotos(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessagesFilter`.

    Details:
        - Layer: ``224``
        - ID: ``9609A51C``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x9609a51c
    QUALNAME = "types.InputMessagesFilterPhotos"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMessagesFilterPhotos":
        
        return InputMessagesFilterPhotos()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

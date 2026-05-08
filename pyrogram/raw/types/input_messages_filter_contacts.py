
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMessagesFilterContacts(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessagesFilter`.

    Details:
        - Layer: ``224``
        - ID: ``E062DB83``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xe062db83
    QUALNAME = "types.InputMessagesFilterContacts"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMessagesFilterContacts":
        
        return InputMessagesFilterContacts()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

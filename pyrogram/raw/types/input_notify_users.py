
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputNotifyUsers(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputNotifyPeer`.

    Details:
        - Layer: ``224``
        - ID: ``193B4417``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x193b4417
    QUALNAME = "types.InputNotifyUsers"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputNotifyUsers":
        
        return InputNotifyUsers()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

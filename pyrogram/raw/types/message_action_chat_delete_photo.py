
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageActionChatDeletePhoto(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``95E3FBEF``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x95e3fbef
    QUALNAME = "types.MessageActionChatDeletePhoto"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionChatDeletePhoto":
        
        return MessageActionChatDeletePhoto()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

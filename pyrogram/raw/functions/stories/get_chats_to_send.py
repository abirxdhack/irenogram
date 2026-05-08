
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetChatsToSend(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A56A8B60``

    Parameters:
        No parameters required.

    Returns:
        :obj:`messages.Chats <pyrogram.raw.base.messages.Chats>`
    """

    __slots__: List[str] = []

    ID = 0xa56a8b60
    QUALNAME = "functions.stories.GetChatsToSend"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChatsToSend":
        
        return GetChatsToSend()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

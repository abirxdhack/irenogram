
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetFullChat(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``AEB00B34``

    Parameters:
        chat_id (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`messages.ChatFull <pyrogram.raw.base.messages.ChatFull>`
    """

    __slots__: List[str] = ["chat_id"]

    ID = 0xaeb00b34
    QUALNAME = "functions.messages.GetFullChat"

    def __init__(self, *, chat_id: int) -> None:
        self.chat_id = chat_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFullChat":
        
        chat_id = Long.read(b)
        
        return GetFullChat(chat_id=chat_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.chat_id))
        
        return b.getvalue()

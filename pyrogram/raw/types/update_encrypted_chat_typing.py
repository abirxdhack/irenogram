
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateEncryptedChatTyping(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``1710F156``

    Parameters:
        chat_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["chat_id"]

    ID = 0x1710f156
    QUALNAME = "types.UpdateEncryptedChatTyping"

    def __init__(self, *, chat_id: int) -> None:
        self.chat_id = chat_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateEncryptedChatTyping":
        
        chat_id = Int.read(b)
        
        return UpdateEncryptedChatTyping(chat_id=chat_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.chat_id))
        
        return b.getvalue()

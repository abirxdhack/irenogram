
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateChat(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``F89A6A4E``

    Parameters:
        chat_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["chat_id"]

    ID = 0xf89a6a4e
    QUALNAME = "types.UpdateChat"

    def __init__(self, *, chat_id: int) -> None:
        self.chat_id = chat_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChat":
        
        chat_id = Long.read(b)
        
        return UpdateChat(chat_id=chat_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.chat_id))
        
        return b.getvalue()

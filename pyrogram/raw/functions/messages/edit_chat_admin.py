
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EditChatAdmin(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A85BD1C2``

    Parameters:
        chat_id (``int`` ``64-bit``):
            N/A

        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        is_admin (``bool``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["chat_id", "user_id", "is_admin"]

    ID = 0xa85bd1c2
    QUALNAME = "functions.messages.EditChatAdmin"

    def __init__(self, *, chat_id: int, user_id: "raw.base.InputUser", is_admin: bool) -> None:
        self.chat_id = chat_id
        self.user_id = user_id
        self.is_admin = is_admin

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditChatAdmin":
        
        chat_id = Long.read(b)
        
        user_id = TLObject.read(b)
        
        is_admin = Bool.read(b)
        
        return EditChatAdmin(chat_id=chat_id, user_id=user_id, is_admin=is_admin)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.chat_id))
        
        b.write(self.user_id.write())
        
        b.write(Bool(self.is_admin))
        
        return b.getvalue()

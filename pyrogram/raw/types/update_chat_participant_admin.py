
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateChatParticipantAdmin(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``D7CA61A2``

    Parameters:
        chat_id (``int`` ``64-bit``):
            N/A

        user_id (``int`` ``64-bit``):
            N/A

        is_admin (``bool``):
            N/A

        version (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["chat_id", "user_id", "is_admin", "version"]

    ID = 0xd7ca61a2
    QUALNAME = "types.UpdateChatParticipantAdmin"

    def __init__(self, *, chat_id: int, user_id: int, is_admin: bool, version: int) -> None:
        self.chat_id = chat_id
        self.user_id = user_id
        self.is_admin = is_admin
        self.version = version

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChatParticipantAdmin":
        
        chat_id = Long.read(b)
        
        user_id = Long.read(b)
        
        is_admin = Bool.read(b)
        
        version = Int.read(b)
        
        return UpdateChatParticipantAdmin(chat_id=chat_id, user_id=user_id, is_admin=is_admin, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.chat_id))
        
        b.write(Long(self.user_id))
        
        b.write(Bool(self.is_admin))
        
        b.write(Int(self.version))
        
        return b.getvalue()

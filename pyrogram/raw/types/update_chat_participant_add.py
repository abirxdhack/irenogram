
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateChatParticipantAdd(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``3DDA5451``

    Parameters:
        chat_id (``int`` ``64-bit``):
            N/A

        user_id (``int`` ``64-bit``):
            N/A

        inviter_id (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        version (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["chat_id", "user_id", "inviter_id", "date", "version"]

    ID = 0x3dda5451
    QUALNAME = "types.UpdateChatParticipantAdd"

    def __init__(self, *, chat_id: int, user_id: int, inviter_id: int, date: int, version: int) -> None:
        self.chat_id = chat_id
        self.user_id = user_id
        self.inviter_id = inviter_id
        self.date = date
        self.version = version

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChatParticipantAdd":
        
        chat_id = Long.read(b)
        
        user_id = Long.read(b)
        
        inviter_id = Long.read(b)
        
        date = Int.read(b)
        
        version = Int.read(b)
        
        return UpdateChatParticipantAdd(chat_id=chat_id, user_id=user_id, inviter_id=inviter_id, date=date, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.chat_id))
        
        b.write(Long(self.user_id))
        
        b.write(Long(self.inviter_id))
        
        b.write(Int(self.date))
        
        b.write(Int(self.version))
        
        return b.getvalue()

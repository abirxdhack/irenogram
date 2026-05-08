
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateChatParticipantDelete(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``E32F3D77``

    Parameters:
        chat_id (``int`` ``64-bit``):
            N/A

        user_id (``int`` ``64-bit``):
            N/A

        version (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["chat_id", "user_id", "version"]

    ID = 0xe32f3d77
    QUALNAME = "types.UpdateChatParticipantDelete"

    def __init__(self, *, chat_id: int, user_id: int, version: int) -> None:
        self.chat_id = chat_id
        self.user_id = user_id
        self.version = version

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChatParticipantDelete":
        
        chat_id = Long.read(b)
        
        user_id = Long.read(b)
        
        version = Int.read(b)
        
        return UpdateChatParticipantDelete(chat_id=chat_id, user_id=user_id, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.chat_id))
        
        b.write(Long(self.user_id))
        
        b.write(Int(self.version))
        
        return b.getvalue()

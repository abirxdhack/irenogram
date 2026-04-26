
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateChatParticipantRank(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``BD8367B9``

    Parameters:
        chat_id (``int`` ``64-bit``):
            N/A

        user_id (``int`` ``64-bit``):
            N/A

        rank (``str``):
            N/A

        version (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["chat_id", "user_id", "rank", "version"]

    ID = 0xbd8367b9
    QUALNAME = "types.UpdateChatParticipantRank"

    def __init__(self, *, chat_id: int, user_id: int, rank: str, version: int) -> None:
        self.chat_id = chat_id
        self.user_id = user_id
        self.rank = rank
        self.version = version

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChatParticipantRank":
        
        chat_id = Long.read(b)
        
        user_id = Long.read(b)
        
        rank = String.read(b)
        
        version = Int.read(b)
        
        return UpdateChatParticipantRank(chat_id=chat_id, user_id=user_id, rank=rank, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.chat_id))
        
        b.write(Long(self.user_id))
        
        b.write(String(self.rank))
        
        b.write(Int(self.version))
        
        return b.getvalue()

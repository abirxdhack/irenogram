
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateChatParticipants(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``7761198``

    Parameters:
        participants (:obj:`ChatParticipants <pyrogram.raw.base.ChatParticipants>`):
            N/A

    """

    __slots__: List[str] = ["participants"]

    ID = 0x7761198
    QUALNAME = "types.UpdateChatParticipants"

    def __init__(self, *, participants: "raw.base.ChatParticipants") -> None:
        self.participants = participants

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChatParticipants":
        
        participants = TLObject.read(b)
        
        return UpdateChatParticipants(participants=participants)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.participants.write())
        
        return b.getvalue()

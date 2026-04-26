
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PrivacyValueDisallowChatParticipants(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PrivacyRule`.

    Details:
        - Layer: ``224``
        - ID: ``41C87565``

    Parameters:
        chats (List of ``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["chats"]

    ID = 0x41c87565
    QUALNAME = "types.PrivacyValueDisallowChatParticipants"

    def __init__(self, *, chats: List[int]) -> None:
        self.chats = chats

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PrivacyValueDisallowChatParticipants":
        
        chats = TLObject.read(b, Long)
        
        return PrivacyValueDisallowChatParticipants(chats=chats)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.chats, Long))
        
        return b.getvalue()

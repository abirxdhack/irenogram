
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChatInvitePeek(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatInvite`.

    Details:
        - Layer: ``224``
        - ID: ``61695CB0``

    Parameters:
        chat (:obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        expires (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.CheckChatInvite
    """

    __slots__: List[str] = ["chat", "expires"]

    ID = 0x61695cb0
    QUALNAME = "types.ChatInvitePeek"

    def __init__(self, *, chat: "raw.base.Chat", expires: int) -> None:
        self.chat = chat
        self.expires = expires

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatInvitePeek":
        
        chat = TLObject.read(b)
        
        expires = Int.read(b)
        
        return ChatInvitePeek(chat=chat, expires=expires)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.chat.write())
        
        b.write(Int(self.expires))
        
        return b.getvalue()

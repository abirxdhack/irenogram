
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChatInviteAlready(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatInvite`.

    Details:
        - Layer: ``224``
        - ID: ``5A686D7C``

    Parameters:
        chat (:obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.CheckChatInvite
    """

    __slots__: List[str] = ["chat"]

    ID = 0x5a686d7c
    QUALNAME = "types.ChatInviteAlready"

    def __init__(self, *, chat: "raw.base.Chat") -> None:
        self.chat = chat

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatInviteAlready":
        
        chat = TLObject.read(b)
        
        return ChatInviteAlready(chat=chat)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.chat.write())
        
        return b.getvalue()

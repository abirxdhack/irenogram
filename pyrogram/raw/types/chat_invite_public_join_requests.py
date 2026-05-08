
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChatInvitePublicJoinRequests(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ExportedChatInvite`.

    Details:
        - Layer: ``224``
        - ID: ``ED107AB7``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.ExportChatInvite
    """

    __slots__: List[str] = []

    ID = 0xed107ab7
    QUALNAME = "types.ChatInvitePublicJoinRequests"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatInvitePublicJoinRequests":
        
        return ChatInvitePublicJoinRequests()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()

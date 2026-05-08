
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class Chats(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.Chats`.

    Details:
        - Layer: ``224``
        - ID: ``64FF9FD5``

    Parameters:
        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

    Functions:
        This object can be returned by 8 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetChats
            messages.GetCommonChats
            channels.GetChannels
            channels.GetAdminedPublicChannels
            channels.GetLeftChannels
            channels.GetGroupsForDiscussion
            channels.GetChannelRecommendations
            stories.GetChatsToSend
    """

    __slots__: List[str] = ["chats"]

    ID = 0x64ff9fd5
    QUALNAME = "types.messages.Chats"

    def __init__(self, *, chats: List["raw.base.Chat"]) -> None:
        self.chats = chats

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Chats":
        
        chats = TLObject.read(b)
        
        return Chats(chats=chats)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.chats))
        
        return b.getvalue()

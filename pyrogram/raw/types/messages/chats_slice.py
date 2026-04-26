
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChatsSlice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.Chats`.

    Details:
        - Layer: ``224``
        - ID: ``9CD81144``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

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

    __slots__: List[str] = ["count", "chats"]

    ID = 0x9cd81144
    QUALNAME = "types.messages.ChatsSlice"

    def __init__(self, *, count: int, chats: List["raw.base.Chat"]) -> None:
        self.count = count
        self.chats = chats

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatsSlice":
        
        count = Int.read(b)
        
        chats = TLObject.read(b)
        
        return ChatsSlice(count=count, chats=chats)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.count))
        
        b.write(Vector(self.chats))
        
        return b.getvalue()

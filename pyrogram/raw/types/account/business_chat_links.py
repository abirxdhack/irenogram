
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BusinessChatLinks(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.BusinessChatLinks`.

    Details:
        - Layer: ``224``
        - ID: ``EC43A2D1``

    Parameters:
        links (List of :obj:`BusinessChatLink <pyrogram.raw.base.BusinessChatLink>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetBusinessChatLinks
    """

    __slots__: List[str] = ["links", "chats", "users"]

    ID = 0xec43a2d1
    QUALNAME = "types.account.BusinessChatLinks"

    def __init__(self, *, links: List["raw.base.BusinessChatLink"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.links = links
        self.chats = chats
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessChatLinks":
        
        links = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return BusinessChatLinks(links=links, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.links))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()

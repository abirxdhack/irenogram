
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class TopPeers(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.contacts.TopPeers`.

    Details:
        - Layer: ``224``
        - ID: ``70B772A8``

    Parameters:
        categories (List of :obj:`TopPeerCategoryPeers <pyrogram.raw.base.TopPeerCategoryPeers>`):
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

            contacts.GetTopPeers
    """

    __slots__: List[str] = ["categories", "chats", "users"]

    ID = 0x70b772a8
    QUALNAME = "types.contacts.TopPeers"

    def __init__(self, *, categories: List["raw.base.TopPeerCategoryPeers"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.categories = categories
        self.chats = chats
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TopPeers":
        
        categories = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return TopPeers(categories=categories, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.categories))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()

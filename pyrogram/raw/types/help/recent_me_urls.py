
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RecentMeUrls(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.RecentMeUrls`.

    Details:
        - Layer: ``224``
        - ID: ``E0310D7``

    Parameters:
        urls (List of :obj:`RecentMeUrl <pyrogram.raw.base.RecentMeUrl>`):
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

            help.GetRecentMeUrls
    """

    __slots__: List[str] = ["urls", "chats", "users"]

    ID = 0xe0310d7
    QUALNAME = "types.help.RecentMeUrls"

    def __init__(self, *, urls: List["raw.base.RecentMeUrl"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.urls = urls
        self.chats = chats
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RecentMeUrls":
        
        urls = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return RecentMeUrls(urls=urls, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.urls))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()

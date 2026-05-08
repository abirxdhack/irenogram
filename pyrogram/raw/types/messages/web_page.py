
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class WebPage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.WebPage`.

    Details:
        - Layer: ``224``
        - ID: ``FD5E12BD``

    Parameters:
        webpage (:obj:`WebPage <pyrogram.raw.base.WebPage>`):
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

            messages.GetWebPage
    """

    __slots__: List[str] = ["webpage", "chats", "users"]

    ID = 0xfd5e12bd
    QUALNAME = "types.messages.WebPage"

    def __init__(self, *, webpage: "raw.base.WebPage", chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.webpage = webpage
        self.chats = chats
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPage":
        
        webpage = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return WebPage(webpage=webpage, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.webpage.write())
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()

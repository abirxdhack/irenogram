
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UserFull(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.users.UserFull`.

    Details:
        - Layer: ``224``
        - ID: ``3B6D152E``

    Parameters:
        full_user (:obj:`UserFull <pyrogram.raw.base.UserFull>`):
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

            users.GetFullUser
    """

    __slots__: List[str] = ["full_user", "chats", "users"]

    ID = 0x3b6d152e
    QUALNAME = "types.users.UserFull"

    def __init__(self, *, full_user: "raw.base.UserFull", chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.full_user = full_user
        self.chats = chats
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserFull":
        
        full_user = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return UserFull(full_user=full_user, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.full_user.write())
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()

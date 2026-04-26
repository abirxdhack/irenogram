
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class Users(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.users.Users`.

    Details:
        - Layer: ``224``
        - ID: ``62D706B8``

    Parameters:
        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetBotRecommendations
    """

    __slots__: List[str] = ["users"]

    ID = 0x62d706b8
    QUALNAME = "types.users.Users"

    def __init__(self, *, users: List["raw.base.User"]) -> None:
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Users":
        
        users = TLObject.read(b)
        
        return Users(users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.users))
        
        return b.getvalue()

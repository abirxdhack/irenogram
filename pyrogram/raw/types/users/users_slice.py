
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UsersSlice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.users.Users`.

    Details:
        - Layer: ``224``
        - ID: ``315A4974``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetBotRecommendations
    """

    __slots__: List[str] = ["count", "users"]

    ID = 0x315a4974
    QUALNAME = "types.users.UsersSlice"

    def __init__(self, *, count: int, users: List["raw.base.User"]) -> None:
        self.count = count
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UsersSlice":
        
        count = Int.read(b)
        
        users = TLObject.read(b)
        
        return UsersSlice(count=count, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.count))
        
        b.write(Vector(self.users))
        
        return b.getvalue()

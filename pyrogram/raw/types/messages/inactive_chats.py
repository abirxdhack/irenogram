
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InactiveChats(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.InactiveChats`.

    Details:
        - Layer: ``224``
        - ID: ``A927FEC5``

    Parameters:
        dates (List of ``int`` ``32-bit``):
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

            channels.GetInactiveChannels
    """

    __slots__: List[str] = ["dates", "chats", "users"]

    ID = 0xa927fec5
    QUALNAME = "types.messages.InactiveChats"

    def __init__(self, *, dates: List[int], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.dates = dates
        self.chats = chats
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InactiveChats":
        
        dates = TLObject.read(b, Int)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return InactiveChats(dates=dates, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.dates, Int))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UserEmpty(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.User`.

    Details:
        - Layer: ``224``
        - ID: ``D3BC4B7A``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 9 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.UpdateProfile
            account.UpdateUsername
            account.ChangePhone
            users.GetUsers
            contacts.ImportContactToken
            messages.GetFutureChatCreatorAfterLeave
            channels.GetMessageAuthor
            bots.GetAdminedBots
            bots.CreateBot
    """

    __slots__: List[str] = ["id"]

    ID = 0xd3bc4b7a
    QUALNAME = "types.UserEmpty"

    def __init__(self, *, id: int) -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserEmpty":
        
        id = Long.read(b)
        
        return UserEmpty(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ExportedInvites(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.chatlists.ExportedInvites`.

    Details:
        - Layer: ``224``
        - ID: ``10AB6DC7``

    Parameters:
        invites (List of :obj:`ExportedChatlistInvite <pyrogram.raw.base.ExportedChatlistInvite>`):
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

            chatlists.GetExportedInvites
    """

    __slots__: List[str] = ["invites", "chats", "users"]

    ID = 0x10ab6dc7
    QUALNAME = "types.chatlists.ExportedInvites"

    def __init__(self, *, invites: List["raw.base.ExportedChatlistInvite"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.invites = invites
        self.chats = chats
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedInvites":
        
        invites = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ExportedInvites(invites=invites, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.invites))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ExportedChatInvite(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.ExportedChatInvite`.

    Details:
        - Layer: ``224``
        - ID: ``1871BE50``

    Parameters:
        invite (:obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetExportedChatInvite
            messages.EditExportedChatInvite
    """

    __slots__: List[str] = ["invite", "users"]

    ID = 0x1871be50
    QUALNAME = "types.messages.ExportedChatInvite"

    def __init__(self, *, invite: "raw.base.ExportedChatInvite", users: List["raw.base.User"]) -> None:
        self.invite = invite
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedChatInvite":
        
        invite = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ExportedChatInvite(invite=invite, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.invite.write())
        
        b.write(Vector(self.users))
        
        return b.getvalue()

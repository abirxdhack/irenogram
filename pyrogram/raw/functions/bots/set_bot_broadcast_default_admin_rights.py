
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetBotBroadcastDefaultAdminRights(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``788464E1``

    Parameters:
        admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["admin_rights"]

    ID = 0x788464e1
    QUALNAME = "functions.bots.SetBotBroadcastDefaultAdminRights"

    def __init__(self, *, admin_rights: "raw.base.ChatAdminRights") -> None:
        self.admin_rights = admin_rights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetBotBroadcastDefaultAdminRights":
        
        admin_rights = TLObject.read(b)
        
        return SetBotBroadcastDefaultAdminRights(admin_rights=admin_rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.admin_rights.write())
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RequestPeerTypeBroadcast(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.RequestPeerType`.

    Details:
        - Layer: ``224``
        - ID: ``339BEF6C``

    Parameters:
        creator (``bool``, *optional*):
            N/A

        has_username (``bool``, *optional*):
            N/A

        user_admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`, *optional*):
            N/A

        bot_admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["creator", "has_username", "user_admin_rights", "bot_admin_rights"]

    ID = 0x339bef6c
    QUALNAME = "types.RequestPeerTypeBroadcast"

    def __init__(self, *, creator: Optional[bool] = None, has_username: Optional[bool] = None, user_admin_rights: "raw.base.ChatAdminRights" = None, bot_admin_rights: "raw.base.ChatAdminRights" = None) -> None:
        self.creator = creator
        self.has_username = has_username
        self.user_admin_rights = user_admin_rights
        self.bot_admin_rights = bot_admin_rights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestPeerTypeBroadcast":
        
        flags = Int.read(b)
        
        creator = True if flags & (1 << 0) else False
        has_username = Bool.read(b) if flags & (1 << 3) else None
        user_admin_rights = TLObject.read(b) if flags & (1 << 1) else None
        
        bot_admin_rights = TLObject.read(b) if flags & (1 << 2) else None
        
        return RequestPeerTypeBroadcast(creator=creator, has_username=has_username, user_admin_rights=user_admin_rights, bot_admin_rights=bot_admin_rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.creator else 0
        flags |= (1 << 3) if self.has_username is not None else 0
        flags |= (1 << 1) if self.user_admin_rights is not None else 0
        flags |= (1 << 2) if self.bot_admin_rights is not None else 0
        b.write(Int(flags))
        
        if self.has_username is not None:
            b.write(Bool(self.has_username))
        
        if self.user_admin_rights is not None:
            b.write(self.user_admin_rights.write())
        
        if self.bot_admin_rights is not None:
            b.write(self.bot_admin_rights.write())
        
        return b.getvalue()

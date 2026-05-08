
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EditAdmin(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``9A98AD68``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`):
            N/A

        rank (``str``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "user_id", "admin_rights", "rank"]

    ID = 0x9a98ad68
    QUALNAME = "functions.channels.EditAdmin"

    def __init__(self, *, channel: "raw.base.InputChannel", user_id: "raw.base.InputUser", admin_rights: "raw.base.ChatAdminRights", rank: Optional[str] = None) -> None:
        self.channel = channel
        self.user_id = user_id
        self.admin_rights = admin_rights
        self.rank = rank

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditAdmin":
        
        flags = Int.read(b)
        
        channel = TLObject.read(b)
        
        user_id = TLObject.read(b)
        
        admin_rights = TLObject.read(b)
        
        rank = String.read(b) if flags & (1 << 0) else None
        return EditAdmin(channel=channel, user_id=user_id, admin_rights=admin_rights, rank=rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.rank is not None else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(self.user_id.write())
        
        b.write(self.admin_rights.write())
        
        if self.rank is not None:
            b.write(String(self.rank))
        
        return b.getvalue()

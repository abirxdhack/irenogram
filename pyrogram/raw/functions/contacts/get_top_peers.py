
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetTopPeers(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``973478B6``

    Parameters:
        offset (``int`` ``32-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        hash (``int`` ``64-bit``):
            N/A

        correspondents (``bool``, *optional*):
            N/A

        bots_pm (``bool``, *optional*):
            N/A

        bots_inline (``bool``, *optional*):
            N/A

        phone_calls (``bool``, *optional*):
            N/A

        forward_users (``bool``, *optional*):
            N/A

        forward_chats (``bool``, *optional*):
            N/A

        groups (``bool``, *optional*):
            N/A

        channels (``bool``, *optional*):
            N/A

        bots_app (``bool``, *optional*):
            N/A

    Returns:
        :obj:`contacts.TopPeers <pyrogram.raw.base.contacts.TopPeers>`
    """

    __slots__: List[str] = ["offset", "limit", "hash", "correspondents", "bots_pm", "bots_inline", "phone_calls", "forward_users", "forward_chats", "groups", "channels", "bots_app"]

    ID = 0x973478b6
    QUALNAME = "functions.contacts.GetTopPeers"

    def __init__(self, *, offset: int, limit: int, hash: int, correspondents: Optional[bool] = None, bots_pm: Optional[bool] = None, bots_inline: Optional[bool] = None, phone_calls: Optional[bool] = None, forward_users: Optional[bool] = None, forward_chats: Optional[bool] = None, groups: Optional[bool] = None, channels: Optional[bool] = None, bots_app: Optional[bool] = None) -> None:
        self.offset = offset
        self.limit = limit
        self.hash = hash
        self.correspondents = correspondents
        self.bots_pm = bots_pm
        self.bots_inline = bots_inline
        self.phone_calls = phone_calls
        self.forward_users = forward_users
        self.forward_chats = forward_chats
        self.groups = groups
        self.channels = channels
        self.bots_app = bots_app

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetTopPeers":
        
        flags = Int.read(b)
        
        correspondents = True if flags & (1 << 0) else False
        bots_pm = True if flags & (1 << 1) else False
        bots_inline = True if flags & (1 << 2) else False
        phone_calls = True if flags & (1 << 3) else False
        forward_users = True if flags & (1 << 4) else False
        forward_chats = True if flags & (1 << 5) else False
        groups = True if flags & (1 << 10) else False
        channels = True if flags & (1 << 15) else False
        bots_app = True if flags & (1 << 16) else False
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        hash = Long.read(b)
        
        return GetTopPeers(offset=offset, limit=limit, hash=hash, correspondents=correspondents, bots_pm=bots_pm, bots_inline=bots_inline, phone_calls=phone_calls, forward_users=forward_users, forward_chats=forward_chats, groups=groups, channels=channels, bots_app=bots_app)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.correspondents else 0
        flags |= (1 << 1) if self.bots_pm else 0
        flags |= (1 << 2) if self.bots_inline else 0
        flags |= (1 << 3) if self.phone_calls else 0
        flags |= (1 << 4) if self.forward_users else 0
        flags |= (1 << 5) if self.forward_chats else 0
        flags |= (1 << 10) if self.groups else 0
        flags |= (1 << 15) if self.channels else 0
        flags |= (1 << 16) if self.bots_app else 0
        b.write(Int(flags))
        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        b.write(Long(self.hash))
        
        return b.getvalue()

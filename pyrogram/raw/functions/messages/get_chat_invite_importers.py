
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetChatInviteImporters(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``DF04DD4E``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        offset_date (``int`` ``32-bit``):
            N/A

        offset_user (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        requested (``bool``, *optional*):
            N/A

        subscription_expired (``bool``, *optional*):
            N/A

        link (``str``, *optional*):
            N/A

        q (``str``, *optional*):
            N/A

    Returns:
        :obj:`messages.ChatInviteImporters <pyrogram.raw.base.messages.ChatInviteImporters>`
    """

    __slots__: List[str] = ["peer", "offset_date", "offset_user", "limit", "requested", "subscription_expired", "link", "q"]

    ID = 0xdf04dd4e
    QUALNAME = "functions.messages.GetChatInviteImporters"

    def __init__(self, *, peer: "raw.base.InputPeer", offset_date: int, offset_user: "raw.base.InputUser", limit: int, requested: Optional[bool] = None, subscription_expired: Optional[bool] = None, link: Optional[str] = None, q: Optional[str] = None) -> None:
        self.peer = peer
        self.offset_date = offset_date
        self.offset_user = offset_user
        self.limit = limit
        self.requested = requested
        self.subscription_expired = subscription_expired
        self.link = link
        self.q = q

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChatInviteImporters":
        
        flags = Int.read(b)
        
        requested = True if flags & (1 << 0) else False
        subscription_expired = True if flags & (1 << 3) else False
        peer = TLObject.read(b)
        
        link = String.read(b) if flags & (1 << 1) else None
        q = String.read(b) if flags & (1 << 2) else None
        offset_date = Int.read(b)
        
        offset_user = TLObject.read(b)
        
        limit = Int.read(b)
        
        return GetChatInviteImporters(peer=peer, offset_date=offset_date, offset_user=offset_user, limit=limit, requested=requested, subscription_expired=subscription_expired, link=link, q=q)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.requested else 0
        flags |= (1 << 3) if self.subscription_expired else 0
        flags |= (1 << 1) if self.link is not None else 0
        flags |= (1 << 2) if self.q is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.link is not None:
            b.write(String(self.link))
        
        if self.q is not None:
            b.write(String(self.q))
        
        b.write(Int(self.offset_date))
        
        b.write(self.offset_user.write())
        
        b.write(Int(self.limit))
        
        return b.getvalue()

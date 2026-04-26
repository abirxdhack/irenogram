
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SearchGlobal(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``4BC6589A``

    Parameters:
        q (``str``):
            N/A

        filter (:obj:`MessagesFilter <pyrogram.raw.base.MessagesFilter>`):
            N/A

        min_date (``int`` ``32-bit``):
            N/A

        max_date (``int`` ``32-bit``):
            N/A

        offset_rate (``int`` ``32-bit``):
            N/A

        offset_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        offset_id (``int`` ``32-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        broadcasts_only (``bool``, *optional*):
            N/A

        groups_only (``bool``, *optional*):
            N/A

        users_only (``bool``, *optional*):
            N/A

        folder_id (``int`` ``32-bit``, *optional*):
            N/A

    Returns:
        :obj:`messages.Messages <pyrogram.raw.base.messages.Messages>`
    """

    __slots__: List[str] = ["q", "filter", "min_date", "max_date", "offset_rate", "offset_peer", "offset_id", "limit", "broadcasts_only", "groups_only", "users_only", "folder_id"]

    ID = 0x4bc6589a
    QUALNAME = "functions.messages.SearchGlobal"

    def __init__(self, *, q: str, filter: "raw.base.MessagesFilter", min_date: int, max_date: int, offset_rate: int, offset_peer: "raw.base.InputPeer", offset_id: int, limit: int, broadcasts_only: Optional[bool] = None, groups_only: Optional[bool] = None, users_only: Optional[bool] = None, folder_id: Optional[int] = None) -> None:
        self.q = q
        self.filter = filter
        self.min_date = min_date
        self.max_date = max_date
        self.offset_rate = offset_rate
        self.offset_peer = offset_peer
        self.offset_id = offset_id
        self.limit = limit
        self.broadcasts_only = broadcasts_only
        self.groups_only = groups_only
        self.users_only = users_only
        self.folder_id = folder_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchGlobal":
        
        flags = Int.read(b)
        
        broadcasts_only = True if flags & (1 << 1) else False
        groups_only = True if flags & (1 << 2) else False
        users_only = True if flags & (1 << 3) else False
        folder_id = Int.read(b) if flags & (1 << 0) else None
        q = String.read(b)
        
        filter = TLObject.read(b)
        
        min_date = Int.read(b)
        
        max_date = Int.read(b)
        
        offset_rate = Int.read(b)
        
        offset_peer = TLObject.read(b)
        
        offset_id = Int.read(b)
        
        limit = Int.read(b)
        
        return SearchGlobal(q=q, filter=filter, min_date=min_date, max_date=max_date, offset_rate=offset_rate, offset_peer=offset_peer, offset_id=offset_id, limit=limit, broadcasts_only=broadcasts_only, groups_only=groups_only, users_only=users_only, folder_id=folder_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.broadcasts_only else 0
        flags |= (1 << 2) if self.groups_only else 0
        flags |= (1 << 3) if self.users_only else 0
        flags |= (1 << 0) if self.folder_id is not None else 0
        b.write(Int(flags))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        b.write(String(self.q))
        
        b.write(self.filter.write())
        
        b.write(Int(self.min_date))
        
        b.write(Int(self.max_date))
        
        b.write(Int(self.offset_rate))
        
        b.write(self.offset_peer.write())
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()

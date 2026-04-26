
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CreateChannel(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``91006707``

    Parameters:
        title (``str``):
            N/A

        about (``str``):
            N/A

        broadcast (``bool``, *optional*):
            N/A

        megagroup (``bool``, *optional*):
            N/A

        for_import (``bool``, *optional*):
            N/A

        forum (``bool``, *optional*):
            N/A

        geo_point (:obj:`InputGeoPoint <pyrogram.raw.base.InputGeoPoint>`, *optional*):
            N/A

        address (``str``, *optional*):
            N/A

        ttl_period (``int`` ``32-bit``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["title", "about", "broadcast", "megagroup", "for_import", "forum", "geo_point", "address", "ttl_period"]

    ID = 0x91006707
    QUALNAME = "functions.channels.CreateChannel"

    def __init__(self, *, title: str, about: str, broadcast: Optional[bool] = None, megagroup: Optional[bool] = None, for_import: Optional[bool] = None, forum: Optional[bool] = None, geo_point: "raw.base.InputGeoPoint" = None, address: Optional[str] = None, ttl_period: Optional[int] = None) -> None:
        self.title = title
        self.about = about
        self.broadcast = broadcast
        self.megagroup = megagroup
        self.for_import = for_import
        self.forum = forum
        self.geo_point = geo_point
        self.address = address
        self.ttl_period = ttl_period

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateChannel":
        
        flags = Int.read(b)
        
        broadcast = True if flags & (1 << 0) else False
        megagroup = True if flags & (1 << 1) else False
        for_import = True if flags & (1 << 3) else False
        forum = True if flags & (1 << 5) else False
        title = String.read(b)
        
        about = String.read(b)
        
        geo_point = TLObject.read(b) if flags & (1 << 2) else None
        
        address = String.read(b) if flags & (1 << 2) else None
        ttl_period = Int.read(b) if flags & (1 << 4) else None
        return CreateChannel(title=title, about=about, broadcast=broadcast, megagroup=megagroup, for_import=for_import, forum=forum, geo_point=geo_point, address=address, ttl_period=ttl_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.broadcast else 0
        flags |= (1 << 1) if self.megagroup else 0
        flags |= (1 << 3) if self.for_import else 0
        flags |= (1 << 5) if self.forum else 0
        flags |= (1 << 2) if self.geo_point is not None else 0
        flags |= (1 << 2) if self.address is not None else 0
        flags |= (1 << 4) if self.ttl_period is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(String(self.about))
        
        if self.geo_point is not None:
            b.write(self.geo_point.write())
        
        if self.address is not None:
            b.write(String(self.address))
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        return b.getvalue()

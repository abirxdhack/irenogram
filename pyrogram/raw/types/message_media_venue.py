
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageMediaVenue(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``224``
        - ID: ``2EC0533F``

    Parameters:
        geo (:obj:`GeoPoint <pyrogram.raw.base.GeoPoint>`):
            N/A

        title (``str``):
            N/A

        address (``str``):
            N/A

        provider (``str``):
            N/A

        venue_id (``str``):
            N/A

        venue_type (``str``):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["geo", "title", "address", "provider", "venue_id", "venue_type"]

    ID = 0x2ec0533f
    QUALNAME = "types.MessageMediaVenue"

    def __init__(self, *, geo: "raw.base.GeoPoint", title: str, address: str, provider: str, venue_id: str, venue_type: str) -> None:
        self.geo = geo
        self.title = title
        self.address = address
        self.provider = provider
        self.venue_id = venue_id
        self.venue_type = venue_type

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaVenue":
        
        geo = TLObject.read(b)
        
        title = String.read(b)
        
        address = String.read(b)
        
        provider = String.read(b)
        
        venue_id = String.read(b)
        
        venue_type = String.read(b)
        
        return MessageMediaVenue(geo=geo, title=title, address=address, provider=provider, venue_id=venue_id, venue_type=venue_type)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.geo.write())
        
        b.write(String(self.title))
        
        b.write(String(self.address))
        
        b.write(String(self.provider))
        
        b.write(String(self.venue_id))
        
        b.write(String(self.venue_type))
        
        return b.getvalue()

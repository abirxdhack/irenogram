
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MediaAreaVenue(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MediaArea`.

    Details:
        - Layer: ``224``
        - ID: ``BE82DB9C``

    Parameters:
        coordinates (:obj:`MediaAreaCoordinates <pyrogram.raw.base.MediaAreaCoordinates>`):
            N/A

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

    """

    __slots__: List[str] = ["coordinates", "geo", "title", "address", "provider", "venue_id", "venue_type"]

    ID = 0xbe82db9c
    QUALNAME = "types.MediaAreaVenue"

    def __init__(self, *, coordinates: "raw.base.MediaAreaCoordinates", geo: "raw.base.GeoPoint", title: str, address: str, provider: str, venue_id: str, venue_type: str) -> None:
        self.coordinates = coordinates
        self.geo = geo
        self.title = title
        self.address = address
        self.provider = provider
        self.venue_id = venue_id
        self.venue_type = venue_type

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MediaAreaVenue":
        
        coordinates = TLObject.read(b)
        
        geo = TLObject.read(b)
        
        title = String.read(b)
        
        address = String.read(b)
        
        provider = String.read(b)
        
        venue_id = String.read(b)
        
        venue_type = String.read(b)
        
        return MediaAreaVenue(coordinates=coordinates, geo=geo, title=title, address=address, provider=provider, venue_id=venue_id, venue_type=venue_type)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.coordinates.write())
        
        b.write(self.geo.write())
        
        b.write(String(self.title))
        
        b.write(String(self.address))
        
        b.write(String(self.provider))
        
        b.write(String(self.venue_id))
        
        b.write(String(self.venue_type))
        
        return b.getvalue()

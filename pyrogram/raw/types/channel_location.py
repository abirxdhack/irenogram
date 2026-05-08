
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelLocation(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelLocation`.

    Details:
        - Layer: ``224``
        - ID: ``209B82DB``

    Parameters:
        geo_point (:obj:`GeoPoint <pyrogram.raw.base.GeoPoint>`):
            N/A

        address (``str``):
            N/A

    """

    __slots__: List[str] = ["geo_point", "address"]

    ID = 0x209b82db
    QUALNAME = "types.ChannelLocation"

    def __init__(self, *, geo_point: "raw.base.GeoPoint", address: str) -> None:
        self.geo_point = geo_point
        self.address = address

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelLocation":
        
        geo_point = TLObject.read(b)
        
        address = String.read(b)
        
        return ChannelLocation(geo_point=geo_point, address=address)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.geo_point.write())
        
        b.write(String(self.address))
        
        return b.getvalue()

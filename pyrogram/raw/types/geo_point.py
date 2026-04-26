
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GeoPoint(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.GeoPoint`.

    Details:
        - Layer: ``224``
        - ID: ``B2A2F663``

    Parameters:
        long (``float`` ``64-bit``):
            N/A

        lat (``float`` ``64-bit``):
            N/A

        access_hash (``int`` ``64-bit``):
            N/A

        accuracy_radius (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["long", "lat", "access_hash", "accuracy_radius"]

    ID = 0xb2a2f663
    QUALNAME = "types.GeoPoint"

    def __init__(self, *, long: float, lat: float, access_hash: int, accuracy_radius: Optional[int] = None) -> None:
        self.long = long
        self.lat = lat
        self.access_hash = access_hash
        self.accuracy_radius = accuracy_radius

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GeoPoint":
        
        flags = Int.read(b)
        
        long = Double.read(b)
        
        lat = Double.read(b)
        
        access_hash = Long.read(b)
        
        accuracy_radius = Int.read(b) if flags & (1 << 0) else None
        return GeoPoint(long=long, lat=lat, access_hash=access_hash, accuracy_radius=accuracy_radius)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.accuracy_radius is not None else 0
        b.write(Int(flags))
        
        b.write(Double(self.long))
        
        b.write(Double(self.lat))
        
        b.write(Long(self.access_hash))
        
        if self.accuracy_radius is not None:
            b.write(Int(self.accuracy_radius))
        
        return b.getvalue()

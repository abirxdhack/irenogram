
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputGeoPoint(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputGeoPoint`.

    Details:
        - Layer: ``224``
        - ID: ``48222FAF``

    Parameters:
        lat (``float`` ``64-bit``):
            N/A

        long (``float`` ``64-bit``):
            N/A

        accuracy_radius (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["lat", "long", "accuracy_radius"]

    ID = 0x48222faf
    QUALNAME = "types.InputGeoPoint"

    def __init__(self, *, lat: float, long: float, accuracy_radius: Optional[int] = None) -> None:
        self.lat = lat
        self.long = long
        self.accuracy_radius = accuracy_radius

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputGeoPoint":
        
        flags = Int.read(b)
        
        lat = Double.read(b)
        
        long = Double.read(b)
        
        accuracy_radius = Int.read(b) if flags & (1 << 0) else None
        return InputGeoPoint(lat=lat, long=long, accuracy_radius=accuracy_radius)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.accuracy_radius is not None else 0
        b.write(Int(flags))
        
        b.write(Double(self.lat))
        
        b.write(Double(self.long))
        
        if self.accuracy_radius is not None:
            b.write(Int(self.accuracy_radius))
        
        return b.getvalue()

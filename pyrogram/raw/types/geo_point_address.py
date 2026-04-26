
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GeoPointAddress(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.GeoPointAddress`.

    Details:
        - Layer: ``224``
        - ID: ``DE4C5D93``

    Parameters:
        country_iso2 (``str``):
            N/A

        state (``str``, *optional*):
            N/A

        city (``str``, *optional*):
            N/A

        street (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["country_iso2", "state", "city", "street"]

    ID = 0xde4c5d93
    QUALNAME = "types.GeoPointAddress"

    def __init__(self, *, country_iso2: str, state: Optional[str] = None, city: Optional[str] = None, street: Optional[str] = None) -> None:
        self.country_iso2 = country_iso2
        self.state = state
        self.city = city
        self.street = street

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GeoPointAddress":
        
        flags = Int.read(b)
        
        country_iso2 = String.read(b)
        
        state = String.read(b) if flags & (1 << 0) else None
        city = String.read(b) if flags & (1 << 1) else None
        street = String.read(b) if flags & (1 << 2) else None
        return GeoPointAddress(country_iso2=country_iso2, state=state, city=city, street=street)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.state is not None else 0
        flags |= (1 << 1) if self.city is not None else 0
        flags |= (1 << 2) if self.street is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.country_iso2))
        
        if self.state is not None:
            b.write(String(self.state))
        
        if self.city is not None:
            b.write(String(self.city))
        
        if self.street is not None:
            b.write(String(self.street))
        
        return b.getvalue()

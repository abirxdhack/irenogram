
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMediaGeoPoint(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``F9C44144``

    Parameters:
        geo_point (:obj:`InputGeoPoint <pyrogram.raw.base.InputGeoPoint>`):
            N/A

    """

    __slots__: List[str] = ["geo_point"]

    ID = 0xf9c44144
    QUALNAME = "types.InputMediaGeoPoint"

    def __init__(self, *, geo_point: "raw.base.InputGeoPoint") -> None:
        self.geo_point = geo_point

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaGeoPoint":
        
        geo_point = TLObject.read(b)
        
        return InputMediaGeoPoint(geo_point=geo_point)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.geo_point.write())
        
        return b.getvalue()

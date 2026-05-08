
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MediaAreaUrl(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MediaArea`.

    Details:
        - Layer: ``224``
        - ID: ``37381085``

    Parameters:
        coordinates (:obj:`MediaAreaCoordinates <pyrogram.raw.base.MediaAreaCoordinates>`):
            N/A

        url (``str``):
            N/A

    """

    __slots__: List[str] = ["coordinates", "url"]

    ID = 0x37381085
    QUALNAME = "types.MediaAreaUrl"

    def __init__(self, *, coordinates: "raw.base.MediaAreaCoordinates", url: str) -> None:
        self.coordinates = coordinates
        self.url = url

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MediaAreaUrl":
        
        coordinates = TLObject.read(b)
        
        url = String.read(b)
        
        return MediaAreaUrl(coordinates=coordinates, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.coordinates.write())
        
        b.write(String(self.url))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageMediaGeo(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``224``
        - ID: ``56E0D474``

    Parameters:
        geo (:obj:`GeoPoint <pyrogram.raw.base.GeoPoint>`):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["geo"]

    ID = 0x56e0d474
    QUALNAME = "types.MessageMediaGeo"

    def __init__(self, *, geo: "raw.base.GeoPoint") -> None:
        self.geo = geo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaGeo":
        
        geo = TLObject.read(b)
        
        return MessageMediaGeo(geo=geo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.geo.write())
        
        return b.getvalue()

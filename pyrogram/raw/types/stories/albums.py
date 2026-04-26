
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class Albums(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.stories.Albums`.

    Details:
        - Layer: ``224``
        - ID: ``C3987A3A``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        albums (List of :obj:`StoryAlbum <pyrogram.raw.base.StoryAlbum>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.GetAlbums
    """

    __slots__: List[str] = ["hash", "albums"]

    ID = 0xc3987a3a
    QUALNAME = "types.stories.Albums"

    def __init__(self, *, hash: int, albums: List["raw.base.StoryAlbum"]) -> None:
        self.hash = hash
        self.albums = albums

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Albums":
        
        hash = Long.read(b)
        
        albums = TLObject.read(b)
        
        return Albums(hash=hash, albums=albums)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        b.write(Vector(self.albums))
        
        return b.getvalue()

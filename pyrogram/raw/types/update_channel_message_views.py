
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateChannelMessageViews(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``F226AC08``

    Parameters:
        channel_id (``int`` ``64-bit``):
            N/A

        id (``int`` ``32-bit``):
            N/A

        views (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["channel_id", "id", "views"]

    ID = 0xf226ac08
    QUALNAME = "types.UpdateChannelMessageViews"

    def __init__(self, *, channel_id: int, id: int, views: int) -> None:
        self.channel_id = channel_id
        self.id = id
        self.views = views

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelMessageViews":
        
        channel_id = Long.read(b)
        
        id = Int.read(b)
        
        views = Int.read(b)
        
        return UpdateChannelMessageViews(channel_id=channel_id, id=id, views=views)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.channel_id))
        
        b.write(Int(self.id))
        
        b.write(Int(self.views))
        
        return b.getvalue()

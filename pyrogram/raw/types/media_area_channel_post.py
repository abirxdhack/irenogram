
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MediaAreaChannelPost(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MediaArea`.

    Details:
        - Layer: ``224``
        - ID: ``770416AF``

    Parameters:
        coordinates (:obj:`MediaAreaCoordinates <pyrogram.raw.base.MediaAreaCoordinates>`):
            N/A

        channel_id (``int`` ``64-bit``):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["coordinates", "channel_id", "msg_id"]

    ID = 0x770416af
    QUALNAME = "types.MediaAreaChannelPost"

    def __init__(self, *, coordinates: "raw.base.MediaAreaCoordinates", channel_id: int, msg_id: int) -> None:
        self.coordinates = coordinates
        self.channel_id = channel_id
        self.msg_id = msg_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MediaAreaChannelPost":
        
        coordinates = TLObject.read(b)
        
        channel_id = Long.read(b)
        
        msg_id = Int.read(b)
        
        return MediaAreaChannelPost(coordinates=coordinates, channel_id=channel_id, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.coordinates.write())
        
        b.write(Long(self.channel_id))
        
        b.write(Int(self.msg_id))
        
        return b.getvalue()

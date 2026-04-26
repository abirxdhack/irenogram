
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMediaAreaChannelPost(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MediaArea`.

    Details:
        - Layer: ``224``
        - ID: ``2271F2BF``

    Parameters:
        coordinates (:obj:`MediaAreaCoordinates <pyrogram.raw.base.MediaAreaCoordinates>`):
            N/A

        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["coordinates", "channel", "msg_id"]

    ID = 0x2271f2bf
    QUALNAME = "types.InputMediaAreaChannelPost"

    def __init__(self, *, coordinates: "raw.base.MediaAreaCoordinates", channel: "raw.base.InputChannel", msg_id: int) -> None:
        self.coordinates = coordinates
        self.channel = channel
        self.msg_id = msg_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaAreaChannelPost":
        
        coordinates = TLObject.read(b)
        
        channel = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        return InputMediaAreaChannelPost(coordinates=coordinates, channel=channel, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.coordinates.write())
        
        b.write(self.channel.write())
        
        b.write(Int(self.msg_id))
        
        return b.getvalue()

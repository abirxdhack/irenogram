
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetMessages(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``AD8C9A23``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        id (List of :obj:`InputMessage <pyrogram.raw.base.InputMessage>`):
            N/A

    Returns:
        :obj:`messages.Messages <pyrogram.raw.base.messages.Messages>`
    """

    __slots__: List[str] = ["channel", "id"]

    ID = 0xad8c9a23
    QUALNAME = "functions.channels.GetMessages"

    def __init__(self, *, channel: "raw.base.InputChannel", id: List["raw.base.InputMessage"]) -> None:
        self.channel = channel
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessages":
        
        channel = TLObject.read(b)
        
        id = TLObject.read(b)
        
        return GetMessages(channel=channel, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        b.write(Vector(self.id))
        
        return b.getvalue()

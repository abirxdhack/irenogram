
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DeleteMessages(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``84C1FD4E``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        id (List of ``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.AffectedMessages <pyrogram.raw.base.messages.AffectedMessages>`
    """

    __slots__: List[str] = ["channel", "id"]

    ID = 0x84c1fd4e
    QUALNAME = "functions.channels.DeleteMessages"

    def __init__(self, *, channel: "raw.base.InputChannel", id: List[int]) -> None:
        self.channel = channel
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteMessages":
        
        channel = TLObject.read(b)
        
        id = TLObject.read(b, Int)
        
        return DeleteMessages(channel=channel, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        b.write(Vector(self.id, Int))
        
        return b.getvalue()

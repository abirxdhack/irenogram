
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReadHistory(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``CC104937``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        max_id (``int`` ``32-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "max_id"]

    ID = 0xcc104937
    QUALNAME = "functions.channels.ReadHistory"

    def __init__(self, *, channel: "raw.base.InputChannel", max_id: int) -> None:
        self.channel = channel
        self.max_id = max_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReadHistory":
        
        channel = TLObject.read(b)
        
        max_id = Int.read(b)
        
        return ReadHistory(channel=channel, max_id=max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        b.write(Int(self.max_id))
        
        return b.getvalue()

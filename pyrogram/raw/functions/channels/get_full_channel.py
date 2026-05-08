
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetFullChannel(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``8736A09``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

    Returns:
        :obj:`messages.ChatFull <pyrogram.raw.base.messages.ChatFull>`
    """

    __slots__: List[str] = ["channel"]

    ID = 0x8736a09
    QUALNAME = "functions.channels.GetFullChannel"

    def __init__(self, *, channel: "raw.base.InputChannel") -> None:
        self.channel = channel

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFullChannel":
        
        channel = TLObject.read(b)
        
        return GetFullChannel(channel=channel)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        return b.getvalue()

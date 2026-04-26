
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class LeaveChannel(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``F836AA95``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel"]

    ID = 0xf836aa95
    QUALNAME = "functions.channels.LeaveChannel"

    def __init__(self, *, channel: "raw.base.InputChannel") -> None:
        self.channel = channel

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LeaveChannel":
        
        channel = TLObject.read(b)
        
        return LeaveChannel(channel=channel)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        return b.getvalue()

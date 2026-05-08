
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReportAntiSpamFalsePositive(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A850A693``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "msg_id"]

    ID = 0xa850a693
    QUALNAME = "functions.channels.ReportAntiSpamFalsePositive"

    def __init__(self, *, channel: "raw.base.InputChannel", msg_id: int) -> None:
        self.channel = channel
        self.msg_id = msg_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportAntiSpamFalsePositive":
        
        channel = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        return ReportAntiSpamFalsePositive(channel=channel, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        b.write(Int(self.msg_id))
        
        return b.getvalue()

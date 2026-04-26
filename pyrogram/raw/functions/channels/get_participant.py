
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetParticipant(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A0AB6CC6``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        participant (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    Returns:
        :obj:`channels.ChannelParticipant <pyrogram.raw.base.channels.ChannelParticipant>`
    """

    __slots__: List[str] = ["channel", "participant"]

    ID = 0xa0ab6cc6
    QUALNAME = "functions.channels.GetParticipant"

    def __init__(self, *, channel: "raw.base.InputChannel", participant: "raw.base.InputPeer") -> None:
        self.channel = channel
        self.participant = participant

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetParticipant":
        
        channel = TLObject.read(b)
        
        participant = TLObject.read(b)
        
        return GetParticipant(channel=channel, participant=participant)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        b.write(self.participant.write())
        
        return b.getvalue()

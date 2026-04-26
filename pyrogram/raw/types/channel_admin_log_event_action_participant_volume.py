
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionParticipantVolume(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``3E7F6847``

    Parameters:
        participant (:obj:`GroupCallParticipant <pyrogram.raw.base.GroupCallParticipant>`):
            N/A

    """

    __slots__: List[str] = ["participant"]

    ID = 0x3e7f6847
    QUALNAME = "types.ChannelAdminLogEventActionParticipantVolume"

    def __init__(self, *, participant: "raw.base.GroupCallParticipant") -> None:
        self.participant = participant

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionParticipantVolume":
        
        participant = TLObject.read(b)
        
        return ChannelAdminLogEventActionParticipantVolume(participant=participant)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.participant.write())
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionParticipantUnmute(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``E64429C0``

    Parameters:
        participant (:obj:`GroupCallParticipant <pyrogram.raw.base.GroupCallParticipant>`):
            N/A

    """

    __slots__: List[str] = ["participant"]

    ID = 0xe64429c0
    QUALNAME = "types.ChannelAdminLogEventActionParticipantUnmute"

    def __init__(self, *, participant: "raw.base.GroupCallParticipant") -> None:
        self.participant = participant

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionParticipantUnmute":
        
        participant = TLObject.read(b)
        
        return ChannelAdminLogEventActionParticipantUnmute(participant=participant)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.participant.write())
        
        return b.getvalue()

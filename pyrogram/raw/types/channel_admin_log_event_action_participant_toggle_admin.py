
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionParticipantToggleAdmin(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``D5676710``

    Parameters:
        prev_participant (:obj:`ChannelParticipant <pyrogram.raw.base.ChannelParticipant>`):
            N/A

        new_participant (:obj:`ChannelParticipant <pyrogram.raw.base.ChannelParticipant>`):
            N/A

    """

    __slots__: List[str] = ["prev_participant", "new_participant"]

    ID = 0xd5676710
    QUALNAME = "types.ChannelAdminLogEventActionParticipantToggleAdmin"

    def __init__(self, *, prev_participant: "raw.base.ChannelParticipant", new_participant: "raw.base.ChannelParticipant") -> None:
        self.prev_participant = prev_participant
        self.new_participant = new_participant

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionParticipantToggleAdmin":
        
        prev_participant = TLObject.read(b)
        
        new_participant = TLObject.read(b)
        
        return ChannelAdminLogEventActionParticipantToggleAdmin(prev_participant=prev_participant, new_participant=new_participant)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.prev_participant.write())
        
        b.write(self.new_participant.write())
        
        return b.getvalue()

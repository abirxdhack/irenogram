
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionParticipantInvite(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``E31C34D8``

    Parameters:
        participant (:obj:`ChannelParticipant <pyrogram.raw.base.ChannelParticipant>`):
            N/A

    """

    __slots__: List[str] = ["participant"]

    ID = 0xe31c34d8
    QUALNAME = "types.ChannelAdminLogEventActionParticipantInvite"

    def __init__(self, *, participant: "raw.base.ChannelParticipant") -> None:
        self.participant = participant

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionParticipantInvite":
        
        participant = TLObject.read(b)
        
        return ChannelAdminLogEventActionParticipantInvite(participant=participant)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.participant.write())
        
        return b.getvalue()

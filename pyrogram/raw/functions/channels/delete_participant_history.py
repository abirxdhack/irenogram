
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DeleteParticipantHistory(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``367544DB``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        participant (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    Returns:
        :obj:`messages.AffectedHistory <pyrogram.raw.base.messages.AffectedHistory>`
    """

    __slots__: List[str] = ["channel", "participant"]

    ID = 0x367544db
    QUALNAME = "functions.channels.DeleteParticipantHistory"

    def __init__(self, *, channel: "raw.base.InputChannel", participant: "raw.base.InputPeer") -> None:
        self.channel = channel
        self.participant = participant

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteParticipantHistory":
        
        channel = TLObject.read(b)
        
        participant = TLObject.read(b)
        
        return DeleteParticipantHistory(channel=channel, participant=participant)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        b.write(self.participant.write())
        
        return b.getvalue()

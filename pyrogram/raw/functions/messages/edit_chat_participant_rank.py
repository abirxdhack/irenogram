
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EditChatParticipantRank(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A00F32B0``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        participant (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        rank (``str``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "participant", "rank"]

    ID = 0xa00f32b0
    QUALNAME = "functions.messages.EditChatParticipantRank"

    def __init__(self, *, peer: "raw.base.InputPeer", participant: "raw.base.InputPeer", rank: str) -> None:
        self.peer = peer
        self.participant = participant
        self.rank = rank

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditChatParticipantRank":
        
        peer = TLObject.read(b)
        
        participant = TLObject.read(b)
        
        rank = String.read(b)
        
        return EditChatParticipantRank(peer=peer, participant=participant, rank=rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(self.participant.write())
        
        b.write(String(self.rank))
        
        return b.getvalue()

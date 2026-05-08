
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelParticipant(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.channels.ChannelParticipant`.

    Details:
        - Layer: ``224``
        - ID: ``DFB80317``

    Parameters:
        participant (:obj:`ChannelParticipant <pyrogram.raw.base.ChannelParticipant>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            channels.GetParticipant
    """

    __slots__: List[str] = ["participant", "chats", "users"]

    ID = 0xdfb80317
    QUALNAME = "types.channels.ChannelParticipant"

    def __init__(self, *, participant: "raw.base.ChannelParticipant", chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.participant = participant
        self.chats = chats
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipant":
        
        participant = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ChannelParticipant(participant=participant, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.participant.write())
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateChannelParticipant(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``985D3ABB``

    Parameters:
        channel_id (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        actor_id (``int`` ``64-bit``):
            N/A

        user_id (``int`` ``64-bit``):
            N/A

        qts (``int`` ``32-bit``):
            N/A

        via_chatlist (``bool``, *optional*):
            N/A

        prev_participant (:obj:`ChannelParticipant <pyrogram.raw.base.ChannelParticipant>`, *optional*):
            N/A

        new_participant (:obj:`ChannelParticipant <pyrogram.raw.base.ChannelParticipant>`, *optional*):
            N/A

        invite (:obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["channel_id", "date", "actor_id", "user_id", "qts", "via_chatlist", "prev_participant", "new_participant", "invite"]

    ID = 0x985d3abb
    QUALNAME = "types.UpdateChannelParticipant"

    def __init__(self, *, channel_id: int, date: int, actor_id: int, user_id: int, qts: int, via_chatlist: Optional[bool] = None, prev_participant: "raw.base.ChannelParticipant" = None, new_participant: "raw.base.ChannelParticipant" = None, invite: "raw.base.ExportedChatInvite" = None) -> None:
        self.channel_id = channel_id
        self.date = date
        self.actor_id = actor_id
        self.user_id = user_id
        self.qts = qts
        self.via_chatlist = via_chatlist
        self.prev_participant = prev_participant
        self.new_participant = new_participant
        self.invite = invite

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelParticipant":
        
        flags = Int.read(b)
        
        via_chatlist = True if flags & (1 << 3) else False
        channel_id = Long.read(b)
        
        date = Int.read(b)
        
        actor_id = Long.read(b)
        
        user_id = Long.read(b)
        
        prev_participant = TLObject.read(b) if flags & (1 << 0) else None
        
        new_participant = TLObject.read(b) if flags & (1 << 1) else None
        
        invite = TLObject.read(b) if flags & (1 << 2) else None
        
        qts = Int.read(b)
        
        return UpdateChannelParticipant(channel_id=channel_id, date=date, actor_id=actor_id, user_id=user_id, qts=qts, via_chatlist=via_chatlist, prev_participant=prev_participant, new_participant=new_participant, invite=invite)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.via_chatlist else 0
        flags |= (1 << 0) if self.prev_participant is not None else 0
        flags |= (1 << 1) if self.new_participant is not None else 0
        flags |= (1 << 2) if self.invite is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.channel_id))
        
        b.write(Int(self.date))
        
        b.write(Long(self.actor_id))
        
        b.write(Long(self.user_id))
        
        if self.prev_participant is not None:
            b.write(self.prev_participant.write())
        
        if self.new_participant is not None:
            b.write(self.new_participant.write())
        
        if self.invite is not None:
            b.write(self.invite.write())
        
        b.write(Int(self.qts))
        
        return b.getvalue()

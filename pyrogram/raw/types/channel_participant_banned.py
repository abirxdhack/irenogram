
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelParticipantBanned(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelParticipant`.

    Details:
        - Layer: ``224``
        - ID: ``D5F0AD91``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        kicked_by (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        banned_rights (:obj:`ChatBannedRights <pyrogram.raw.base.ChatBannedRights>`):
            N/A

        left (``bool``, *optional*):
            N/A

        rank (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "kicked_by", "date", "banned_rights", "left", "rank"]

    ID = 0xd5f0ad91
    QUALNAME = "types.ChannelParticipantBanned"

    def __init__(self, *, peer: "raw.base.Peer", kicked_by: int, date: int, banned_rights: "raw.base.ChatBannedRights", left: Optional[bool] = None, rank: Optional[str] = None) -> None:
        self.peer = peer
        self.kicked_by = kicked_by
        self.date = date
        self.banned_rights = banned_rights
        self.left = left
        self.rank = rank

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipantBanned":
        
        flags = Int.read(b)
        
        left = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        kicked_by = Long.read(b)
        
        date = Int.read(b)
        
        banned_rights = TLObject.read(b)
        
        rank = String.read(b) if flags & (1 << 2) else None
        return ChannelParticipantBanned(peer=peer, kicked_by=kicked_by, date=date, banned_rights=banned_rights, left=left, rank=rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.left else 0
        flags |= (1 << 2) if self.rank is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Long(self.kicked_by))
        
        b.write(Int(self.date))
        
        b.write(self.banned_rights.write())
        
        if self.rank is not None:
            b.write(String(self.rank))
        
        return b.getvalue()

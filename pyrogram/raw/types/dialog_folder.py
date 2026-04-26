
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DialogFolder(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Dialog`.

    Details:
        - Layer: ``224``
        - ID: ``71BD134C``

    Parameters:
        folder (:obj:`Folder <pyrogram.raw.base.Folder>`):
            N/A

        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        top_message (``int`` ``32-bit``):
            N/A

        unread_muted_peers_count (``int`` ``32-bit``):
            N/A

        unread_unmuted_peers_count (``int`` ``32-bit``):
            N/A

        unread_muted_messages_count (``int`` ``32-bit``):
            N/A

        unread_unmuted_messages_count (``int`` ``32-bit``):
            N/A

        pinned (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["folder", "peer", "top_message", "unread_muted_peers_count", "unread_unmuted_peers_count", "unread_muted_messages_count", "unread_unmuted_messages_count", "pinned"]

    ID = 0x71bd134c
    QUALNAME = "types.DialogFolder"

    def __init__(self, *, folder: "raw.base.Folder", peer: "raw.base.Peer", top_message: int, unread_muted_peers_count: int, unread_unmuted_peers_count: int, unread_muted_messages_count: int, unread_unmuted_messages_count: int, pinned: Optional[bool] = None) -> None:
        self.folder = folder
        self.peer = peer
        self.top_message = top_message
        self.unread_muted_peers_count = unread_muted_peers_count
        self.unread_unmuted_peers_count = unread_unmuted_peers_count
        self.unread_muted_messages_count = unread_muted_messages_count
        self.unread_unmuted_messages_count = unread_unmuted_messages_count
        self.pinned = pinned

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DialogFolder":
        
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 2) else False
        folder = TLObject.read(b)
        
        peer = TLObject.read(b)
        
        top_message = Int.read(b)
        
        unread_muted_peers_count = Int.read(b)
        
        unread_unmuted_peers_count = Int.read(b)
        
        unread_muted_messages_count = Int.read(b)
        
        unread_unmuted_messages_count = Int.read(b)
        
        return DialogFolder(folder=folder, peer=peer, top_message=top_message, unread_muted_peers_count=unread_muted_peers_count, unread_unmuted_peers_count=unread_unmuted_peers_count, unread_muted_messages_count=unread_muted_messages_count, unread_unmuted_messages_count=unread_unmuted_messages_count, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.pinned else 0
        b.write(Int(flags))
        
        b.write(self.folder.write())
        
        b.write(self.peer.write())
        
        b.write(Int(self.top_message))
        
        b.write(Int(self.unread_muted_peers_count))
        
        b.write(Int(self.unread_unmuted_peers_count))
        
        b.write(Int(self.unread_muted_messages_count))
        
        b.write(Int(self.unread_unmuted_messages_count))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MarkDialogUnread(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``8C5006F8``

    Parameters:
        peer (:obj:`InputDialogPeer <pyrogram.raw.base.InputDialogPeer>`):
            N/A

        unread (``bool``, *optional*):
            N/A

        parent_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "unread", "parent_peer"]

    ID = 0x8c5006f8
    QUALNAME = "functions.messages.MarkDialogUnread"

    def __init__(self, *, peer: "raw.base.InputDialogPeer", unread: Optional[bool] = None, parent_peer: "raw.base.InputPeer" = None) -> None:
        self.peer = peer
        self.unread = unread
        self.parent_peer = parent_peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MarkDialogUnread":
        
        flags = Int.read(b)
        
        unread = True if flags & (1 << 0) else False
        parent_peer = TLObject.read(b) if flags & (1 << 1) else None
        
        peer = TLObject.read(b)
        
        return MarkDialogUnread(peer=peer, unread=unread, parent_peer=parent_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.unread else 0
        flags |= (1 << 1) if self.parent_peer is not None else 0
        b.write(Int(flags))
        
        if self.parent_peer is not None:
            b.write(self.parent_peer.write())
        
        b.write(self.peer.write())
        
        return b.getvalue()

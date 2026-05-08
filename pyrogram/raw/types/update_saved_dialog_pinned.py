
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateSavedDialogPinned(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``AEAF9E74``

    Parameters:
        peer (:obj:`DialogPeer <pyrogram.raw.base.DialogPeer>`):
            N/A

        pinned (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "pinned"]

    ID = 0xaeaf9e74
    QUALNAME = "types.UpdateSavedDialogPinned"

    def __init__(self, *, peer: "raw.base.DialogPeer", pinned: Optional[bool] = None) -> None:
        self.peer = peer
        self.pinned = pinned

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateSavedDialogPinned":
        
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        return UpdateSavedDialogPinned(peer=peer, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pinned else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ToggleSavedDialogPin(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``AC81BBDE``

    Parameters:
        peer (:obj:`InputDialogPeer <pyrogram.raw.base.InputDialogPeer>`):
            N/A

        pinned (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "pinned"]

    ID = 0xac81bbde
    QUALNAME = "functions.messages.ToggleSavedDialogPin"

    def __init__(self, *, peer: "raw.base.InputDialogPeer", pinned: Optional[bool] = None) -> None:
        self.peer = peer
        self.pinned = pinned

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleSavedDialogPin":
        
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        return ToggleSavedDialogPin(peer=peer, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pinned else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        return b.getvalue()

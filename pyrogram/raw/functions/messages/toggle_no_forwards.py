
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ToggleNoForwards(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``B2081A35``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        enabled (``bool``):
            N/A

        request_msg_id (``int`` ``32-bit``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "enabled", "request_msg_id"]

    ID = 0xb2081a35
    QUALNAME = "functions.messages.ToggleNoForwards"

    def __init__(self, *, peer: "raw.base.InputPeer", enabled: bool, request_msg_id: Optional[int] = None) -> None:
        self.peer = peer
        self.enabled = enabled
        self.request_msg_id = request_msg_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleNoForwards":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        enabled = Bool.read(b)
        
        request_msg_id = Int.read(b) if flags & (1 << 0) else None
        return ToggleNoForwards(peer=peer, enabled=enabled, request_msg_id=request_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.request_msg_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Bool(self.enabled))
        
        if self.request_msg_id is not None:
            b.write(Int(self.request_msg_id))
        
        return b.getvalue()

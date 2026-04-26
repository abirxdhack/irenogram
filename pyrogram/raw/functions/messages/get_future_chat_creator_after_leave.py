
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetFutureChatCreatorAfterLeave(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``3B7D0EA6``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    Returns:
        :obj:`User <pyrogram.raw.base.User>`
    """

    __slots__: List[str] = ["peer"]

    ID = 0x3b7d0ea6
    QUALNAME = "functions.messages.GetFutureChatCreatorAfterLeave"

    def __init__(self, *, peer: "raw.base.InputPeer") -> None:
        self.peer = peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFutureChatCreatorAfterLeave":
        
        peer = TLObject.read(b)
        
        return GetFutureChatCreatorAfterLeave(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        return b.getvalue()

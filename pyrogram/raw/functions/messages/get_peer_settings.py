
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetPeerSettings(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``EFD9A6A2``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    Returns:
        :obj:`messages.PeerSettings <pyrogram.raw.base.messages.PeerSettings>`
    """

    __slots__: List[str] = ["peer"]

    ID = 0xefd9a6a2
    QUALNAME = "functions.messages.GetPeerSettings"

    def __init__(self, *, peer: "raw.base.InputPeer") -> None:
        self.peer = peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPeerSettings":
        
        peer = TLObject.read(b)
        
        return GetPeerSettings(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetPeerDialogs(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``E470BCFD``

    Parameters:
        peers (List of :obj:`InputDialogPeer <pyrogram.raw.base.InputDialogPeer>`):
            N/A

    Returns:
        :obj:`messages.PeerDialogs <pyrogram.raw.base.messages.PeerDialogs>`
    """

    __slots__: List[str] = ["peers"]

    ID = 0xe470bcfd
    QUALNAME = "functions.messages.GetPeerDialogs"

    def __init__(self, *, peers: List["raw.base.InputDialogPeer"]) -> None:
        self.peers = peers

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPeerDialogs":
        
        peers = TLObject.read(b)
        
        return GetPeerDialogs(peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.peers))
        
        return b.getvalue()

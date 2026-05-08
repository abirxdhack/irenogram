
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class FulfillStarsSubscription(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``CC5BEBB3``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        subscription_id (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "subscription_id"]

    ID = 0xcc5bebb3
    QUALNAME = "functions.payments.FulfillStarsSubscription"

    def __init__(self, *, peer: "raw.base.InputPeer", subscription_id: str) -> None:
        self.peer = peer
        self.subscription_id = subscription_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FulfillStarsSubscription":
        
        peer = TLObject.read(b)
        
        subscription_id = String.read(b)
        
        return FulfillStarsSubscription(peer=peer, subscription_id=subscription_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(String(self.subscription_id))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SendSignalingData(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``FF7A9383``

    Parameters:
        peer (:obj:`InputPhoneCall <pyrogram.raw.base.InputPhoneCall>`):
            N/A

        data (``bytes``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "data"]

    ID = 0xff7a9383
    QUALNAME = "functions.phone.SendSignalingData"

    def __init__(self, *, peer: "raw.base.InputPhoneCall", data: bytes) -> None:
        self.peer = peer
        self.data = data

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendSignalingData":
        
        peer = TLObject.read(b)
        
        data = Bytes.read(b)
        
        return SendSignalingData(peer=peer, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Bytes(self.data))
        
        return b.getvalue()

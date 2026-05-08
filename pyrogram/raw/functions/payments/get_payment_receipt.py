
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetPaymentReceipt(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``2478D1CC``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`payments.PaymentReceipt <pyrogram.raw.base.payments.PaymentReceipt>`
    """

    __slots__: List[str] = ["peer", "msg_id"]

    ID = 0x2478d1cc
    QUALNAME = "functions.payments.GetPaymentReceipt"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int) -> None:
        self.peer = peer
        self.msg_id = msg_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPaymentReceipt":
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        return GetPaymentReceipt(peer=peer, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        return b.getvalue()

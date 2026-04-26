
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputInvoiceMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``224``
        - ID: ``C5B56859``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["peer", "msg_id"]

    ID = 0xc5b56859
    QUALNAME = "types.InputInvoiceMessage"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int) -> None:
        self.peer = peer
        self.msg_id = msg_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceMessage":
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        return InputInvoiceMessage(peer=peer, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        return b.getvalue()

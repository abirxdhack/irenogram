
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SendConferenceCallBroadcast(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``C6701900``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        block (``bytes``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "block"]

    ID = 0xc6701900
    QUALNAME = "functions.phone.SendConferenceCallBroadcast"

    def __init__(self, *, call: "raw.base.InputGroupCall", block: bytes) -> None:
        self.call = call
        self.block = block

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendConferenceCallBroadcast":
        
        call = TLObject.read(b)
        
        block = Bytes.read(b)
        
        return SendConferenceCallBroadcast(call=call, block=block)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.call.write())
        
        b.write(Bytes(self.block))
        
        return b.getvalue()

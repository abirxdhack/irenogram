
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReceivedCall(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``17D54F61``

    Parameters:
        peer (:obj:`InputPhoneCall <pyrogram.raw.base.InputPhoneCall>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer"]

    ID = 0x17d54f61
    QUALNAME = "functions.phone.ReceivedCall"

    def __init__(self, *, peer: "raw.base.InputPhoneCall") -> None:
        self.peer = peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReceivedCall":
        
        peer = TLObject.read(b)
        
        return ReceivedCall(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        return b.getvalue()

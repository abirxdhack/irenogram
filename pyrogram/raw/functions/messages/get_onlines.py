
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetOnlines(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``6E2BE050``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    Returns:
        :obj:`ChatOnlines <pyrogram.raw.base.ChatOnlines>`
    """

    __slots__: List[str] = ["peer"]

    ID = 0x6e2be050
    QUALNAME = "functions.messages.GetOnlines"

    def __init__(self, *, peer: "raw.base.InputPeer") -> None:
        self.peer = peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetOnlines":
        
        peer = TLObject.read(b)
        
        return GetOnlines(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        return b.getvalue()

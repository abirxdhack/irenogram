
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetPeerProfileColors(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``ABCFA9FD``

    Parameters:
        hash (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`help.PeerColors <pyrogram.raw.base.help.PeerColors>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0xabcfa9fd
    QUALNAME = "functions.help.GetPeerProfileColors"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPeerProfileColors":
        
        hash = Int.read(b)
        
        return GetPeerProfileColors(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.hash))
        
        return b.getvalue()

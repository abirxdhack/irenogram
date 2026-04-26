
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DismissSuggestion(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``F50DBAA1``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        suggestion (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "suggestion"]

    ID = 0xf50dbaa1
    QUALNAME = "functions.help.DismissSuggestion"

    def __init__(self, *, peer: "raw.base.InputPeer", suggestion: str) -> None:
        self.peer = peer
        self.suggestion = suggestion

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DismissSuggestion":
        
        peer = TLObject.read(b)
        
        suggestion = String.read(b)
        
        return DismissSuggestion(peer=peer, suggestion=suggestion)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(String(self.suggestion))
        
        return b.getvalue()

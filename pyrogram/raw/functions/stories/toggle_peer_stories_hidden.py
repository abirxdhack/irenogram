
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class TogglePeerStoriesHidden(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``BD0415C4``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        hidden (``bool``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "hidden"]

    ID = 0xbd0415c4
    QUALNAME = "functions.stories.TogglePeerStoriesHidden"

    def __init__(self, *, peer: "raw.base.InputPeer", hidden: bool) -> None:
        self.peer = peer
        self.hidden = hidden

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TogglePeerStoriesHidden":
        
        peer = TLObject.read(b)
        
        hidden = Bool.read(b)
        
        return TogglePeerStoriesHidden(peer=peer, hidden=hidden)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Bool(self.hidden))
        
        return b.getvalue()

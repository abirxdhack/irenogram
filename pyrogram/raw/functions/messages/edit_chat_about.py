
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EditChatAbout(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``DEF60797``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        about (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "about"]

    ID = 0xdef60797
    QUALNAME = "functions.messages.EditChatAbout"

    def __init__(self, *, peer: "raw.base.InputPeer", about: str) -> None:
        self.peer = peer
        self.about = about

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditChatAbout":
        
        peer = TLObject.read(b)
        
        about = String.read(b)
        
        return EditChatAbout(peer=peer, about=about)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(String(self.about))
        
        return b.getvalue()

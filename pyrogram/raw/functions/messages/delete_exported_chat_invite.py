
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DeleteExportedChatInvite(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D464A42B``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        link (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "link"]

    ID = 0xd464a42b
    QUALNAME = "functions.messages.DeleteExportedChatInvite"

    def __init__(self, *, peer: "raw.base.InputPeer", link: str) -> None:
        self.peer = peer
        self.link = link

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteExportedChatInvite":
        
        peer = TLObject.read(b)
        
        link = String.read(b)
        
        return DeleteExportedChatInvite(peer=peer, link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(String(self.link))
        
        return b.getvalue()

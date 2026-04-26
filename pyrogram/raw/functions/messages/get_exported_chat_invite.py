
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetExportedChatInvite(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``73746F5C``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        link (``str``):
            N/A

    Returns:
        :obj:`messages.ExportedChatInvite <pyrogram.raw.base.messages.ExportedChatInvite>`
    """

    __slots__: List[str] = ["peer", "link"]

    ID = 0x73746f5c
    QUALNAME = "functions.messages.GetExportedChatInvite"

    def __init__(self, *, peer: "raw.base.InputPeer", link: str) -> None:
        self.peer = peer
        self.link = link

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetExportedChatInvite":
        
        peer = TLObject.read(b)
        
        link = String.read(b)
        
        return GetExportedChatInvite(peer=peer, link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(String(self.link))
        
        return b.getvalue()

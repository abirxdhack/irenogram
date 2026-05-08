
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EditChatDefaultBannedRights(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A5866B41``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        banned_rights (:obj:`ChatBannedRights <pyrogram.raw.base.ChatBannedRights>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "banned_rights"]

    ID = 0xa5866b41
    QUALNAME = "functions.messages.EditChatDefaultBannedRights"

    def __init__(self, *, peer: "raw.base.InputPeer", banned_rights: "raw.base.ChatBannedRights") -> None:
        self.peer = peer
        self.banned_rights = banned_rights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditChatDefaultBannedRights":
        
        peer = TLObject.read(b)
        
        banned_rights = TLObject.read(b)
        
        return EditChatDefaultBannedRights(peer=peer, banned_rights=banned_rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(self.banned_rights.write())
        
        return b.getvalue()

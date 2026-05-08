
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class LeaveChatlist(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``74FAE13A``

    Parameters:
        chatlist (:obj:`InputChatlist <pyrogram.raw.base.InputChatlist>`):
            N/A

        peers (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["chatlist", "peers"]

    ID = 0x74fae13a
    QUALNAME = "functions.chatlists.LeaveChatlist"

    def __init__(self, *, chatlist: "raw.base.InputChatlist", peers: List["raw.base.InputPeer"]) -> None:
        self.chatlist = chatlist
        self.peers = peers

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LeaveChatlist":
        
        chatlist = TLObject.read(b)
        
        peers = TLObject.read(b)
        
        return LeaveChatlist(chatlist=chatlist, peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.chatlist.write())
        
        b.write(Vector(self.peers))
        
        return b.getvalue()

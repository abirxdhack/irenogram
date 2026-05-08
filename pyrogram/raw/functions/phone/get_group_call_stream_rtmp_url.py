
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetGroupCallStreamRtmpUrl(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``5AF4C73A``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        revoke (``bool``):
            N/A

        live_story (``bool``, *optional*):
            N/A

    Returns:
        :obj:`phone.GroupCallStreamRtmpUrl <pyrogram.raw.base.phone.GroupCallStreamRtmpUrl>`
    """

    __slots__: List[str] = ["peer", "revoke", "live_story"]

    ID = 0x5af4c73a
    QUALNAME = "functions.phone.GetGroupCallStreamRtmpUrl"

    def __init__(self, *, peer: "raw.base.InputPeer", revoke: bool, live_story: Optional[bool] = None) -> None:
        self.peer = peer
        self.revoke = revoke
        self.live_story = live_story

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGroupCallStreamRtmpUrl":
        
        flags = Int.read(b)
        
        live_story = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        revoke = Bool.read(b)
        
        return GetGroupCallStreamRtmpUrl(peer=peer, revoke=revoke, live_story=live_story)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.live_story else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Bool(self.revoke))
        
        return b.getvalue()

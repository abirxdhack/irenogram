
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DialogFilterChatlist(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DialogFilter`.

    Details:
        - Layer: ``224``
        - ID: ``96537BD7``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        title (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

        pinned_peers (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        include_peers (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        has_my_invites (``bool``, *optional*):
            N/A

        title_noanimate (``bool``, *optional*):
            N/A

        emoticon (``str``, *optional*):
            N/A

        color (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "title", "pinned_peers", "include_peers", "has_my_invites", "title_noanimate", "emoticon", "color"]

    ID = 0x96537bd7
    QUALNAME = "types.DialogFilterChatlist"

    def __init__(self, *, id: int, title: "raw.base.TextWithEntities", pinned_peers: List["raw.base.InputPeer"], include_peers: List["raw.base.InputPeer"], has_my_invites: Optional[bool] = None, title_noanimate: Optional[bool] = None, emoticon: Optional[str] = None, color: Optional[int] = None) -> None:
        self.id = id
        self.title = title
        self.pinned_peers = pinned_peers
        self.include_peers = include_peers
        self.has_my_invites = has_my_invites
        self.title_noanimate = title_noanimate
        self.emoticon = emoticon
        self.color = color

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DialogFilterChatlist":
        
        flags = Int.read(b)
        
        has_my_invites = True if flags & (1 << 26) else False
        title_noanimate = True if flags & (1 << 28) else False
        id = Int.read(b)
        
        title = TLObject.read(b)
        
        emoticon = String.read(b) if flags & (1 << 25) else None
        color = Int.read(b) if flags & (1 << 27) else None
        pinned_peers = TLObject.read(b)
        
        include_peers = TLObject.read(b)
        
        return DialogFilterChatlist(id=id, title=title, pinned_peers=pinned_peers, include_peers=include_peers, has_my_invites=has_my_invites, title_noanimate=title_noanimate, emoticon=emoticon, color=color)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 26) if self.has_my_invites else 0
        flags |= (1 << 28) if self.title_noanimate else 0
        flags |= (1 << 25) if self.emoticon is not None else 0
        flags |= (1 << 27) if self.color is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(self.title.write())
        
        if self.emoticon is not None:
            b.write(String(self.emoticon))
        
        if self.color is not None:
            b.write(Int(self.color))
        
        b.write(Vector(self.pinned_peers))
        
        b.write(Vector(self.include_peers))
        
        return b.getvalue()

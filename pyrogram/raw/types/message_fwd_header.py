
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageFwdHeader(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageFwdHeader`.

    Details:
        - Layer: ``224``
        - ID: ``4E4DF4BB``

    Parameters:
        date (``int`` ``32-bit``):
            N/A

        imported (``bool``, *optional*):
            N/A

        saved_out (``bool``, *optional*):
            N/A

        from_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        from_name (``str``, *optional*):
            N/A

        channel_post (``int`` ``32-bit``, *optional*):
            N/A

        post_author (``str``, *optional*):
            N/A

        saved_from_peer (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        saved_from_msg_id (``int`` ``32-bit``, *optional*):
            N/A

        saved_from_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        saved_from_name (``str``, *optional*):
            N/A

        saved_date (``int`` ``32-bit``, *optional*):
            N/A

        psa_type (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["date", "imported", "saved_out", "from_id", "from_name", "channel_post", "post_author", "saved_from_peer", "saved_from_msg_id", "saved_from_id", "saved_from_name", "saved_date", "psa_type"]

    ID = 0x4e4df4bb
    QUALNAME = "types.MessageFwdHeader"

    def __init__(self, *, date: int, imported: Optional[bool] = None, saved_out: Optional[bool] = None, from_id: "raw.base.Peer" = None, from_name: Optional[str] = None, channel_post: Optional[int] = None, post_author: Optional[str] = None, saved_from_peer: "raw.base.Peer" = None, saved_from_msg_id: Optional[int] = None, saved_from_id: "raw.base.Peer" = None, saved_from_name: Optional[str] = None, saved_date: Optional[int] = None, psa_type: Optional[str] = None) -> None:
        self.date = date
        self.imported = imported
        self.saved_out = saved_out
        self.from_id = from_id
        self.from_name = from_name
        self.channel_post = channel_post
        self.post_author = post_author
        self.saved_from_peer = saved_from_peer
        self.saved_from_msg_id = saved_from_msg_id
        self.saved_from_id = saved_from_id
        self.saved_from_name = saved_from_name
        self.saved_date = saved_date
        self.psa_type = psa_type

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageFwdHeader":
        
        flags = Int.read(b)
        
        imported = True if flags & (1 << 7) else False
        saved_out = True if flags & (1 << 11) else False
        from_id = TLObject.read(b) if flags & (1 << 0) else None
        
        from_name = String.read(b) if flags & (1 << 5) else None
        date = Int.read(b)
        
        channel_post = Int.read(b) if flags & (1 << 2) else None
        post_author = String.read(b) if flags & (1 << 3) else None
        saved_from_peer = TLObject.read(b) if flags & (1 << 4) else None
        
        saved_from_msg_id = Int.read(b) if flags & (1 << 4) else None
        saved_from_id = TLObject.read(b) if flags & (1 << 8) else None
        
        saved_from_name = String.read(b) if flags & (1 << 9) else None
        saved_date = Int.read(b) if flags & (1 << 10) else None
        psa_type = String.read(b) if flags & (1 << 6) else None
        return MessageFwdHeader(date=date, imported=imported, saved_out=saved_out, from_id=from_id, from_name=from_name, channel_post=channel_post, post_author=post_author, saved_from_peer=saved_from_peer, saved_from_msg_id=saved_from_msg_id, saved_from_id=saved_from_id, saved_from_name=saved_from_name, saved_date=saved_date, psa_type=psa_type)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 7) if self.imported else 0
        flags |= (1 << 11) if self.saved_out else 0
        flags |= (1 << 0) if self.from_id is not None else 0
        flags |= (1 << 5) if self.from_name is not None else 0
        flags |= (1 << 2) if self.channel_post is not None else 0
        flags |= (1 << 3) if self.post_author is not None else 0
        flags |= (1 << 4) if self.saved_from_peer is not None else 0
        flags |= (1 << 4) if self.saved_from_msg_id is not None else 0
        flags |= (1 << 8) if self.saved_from_id is not None else 0
        flags |= (1 << 9) if self.saved_from_name is not None else 0
        flags |= (1 << 10) if self.saved_date is not None else 0
        flags |= (1 << 6) if self.psa_type is not None else 0
        b.write(Int(flags))
        
        if self.from_id is not None:
            b.write(self.from_id.write())
        
        if self.from_name is not None:
            b.write(String(self.from_name))
        
        b.write(Int(self.date))
        
        if self.channel_post is not None:
            b.write(Int(self.channel_post))
        
        if self.post_author is not None:
            b.write(String(self.post_author))
        
        if self.saved_from_peer is not None:
            b.write(self.saved_from_peer.write())
        
        if self.saved_from_msg_id is not None:
            b.write(Int(self.saved_from_msg_id))
        
        if self.saved_from_id is not None:
            b.write(self.saved_from_id.write())
        
        if self.saved_from_name is not None:
            b.write(String(self.saved_from_name))
        
        if self.saved_date is not None:
            b.write(Int(self.saved_date))
        
        if self.psa_type is not None:
            b.write(String(self.psa_type))
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RequestedPeerChannel(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.RequestedPeer`.

    Details:
        - Layer: ``224``
        - ID: ``8BA403E4``

    Parameters:
        channel_id (``int`` ``64-bit``):
            N/A

        title (``str``, *optional*):
            N/A

        username (``str``, *optional*):
            N/A

        photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["channel_id", "title", "username", "photo"]

    ID = 0x8ba403e4
    QUALNAME = "types.RequestedPeerChannel"

    def __init__(self, *, channel_id: int, title: Optional[str] = None, username: Optional[str] = None, photo: "raw.base.Photo" = None) -> None:
        self.channel_id = channel_id
        self.title = title
        self.username = username
        self.photo = photo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestedPeerChannel":
        
        flags = Int.read(b)
        
        channel_id = Long.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        username = String.read(b) if flags & (1 << 1) else None
        photo = TLObject.read(b) if flags & (1 << 2) else None
        
        return RequestedPeerChannel(channel_id=channel_id, title=title, username=username, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.username is not None else 0
        flags |= (1 << 2) if self.photo is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.channel_id))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.username is not None:
            b.write(String(self.username))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        return b.getvalue()

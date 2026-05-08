
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RequestedPeerChat(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.RequestedPeer`.

    Details:
        - Layer: ``224``
        - ID: ``7307544F``

    Parameters:
        chat_id (``int`` ``64-bit``):
            N/A

        title (``str``, *optional*):
            N/A

        photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["chat_id", "title", "photo"]

    ID = 0x7307544f
    QUALNAME = "types.RequestedPeerChat"

    def __init__(self, *, chat_id: int, title: Optional[str] = None, photo: "raw.base.Photo" = None) -> None:
        self.chat_id = chat_id
        self.title = title
        self.photo = photo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestedPeerChat":
        
        flags = Int.read(b)
        
        chat_id = Long.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        photo = TLObject.read(b) if flags & (1 << 2) else None
        
        return RequestedPeerChat(chat_id=chat_id, title=title, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 2) if self.photo is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.chat_id))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        return b.getvalue()

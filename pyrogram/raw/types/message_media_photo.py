
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageMediaPhoto(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``224``
        - ID: ``E216EB63``

    Parameters:
        spoiler (``bool``, *optional*):
            N/A

        live_photo (``bool``, *optional*):
            N/A

        photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            N/A

        ttl_seconds (``int`` ``32-bit``, *optional*):
            N/A

        video (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["spoiler", "live_photo", "photo", "ttl_seconds", "video"]

    ID = 0xe216eb63
    QUALNAME = "types.MessageMediaPhoto"

    def __init__(self, *, spoiler: Optional[bool] = None, live_photo: Optional[bool] = None, photo: "raw.base.Photo" = None, ttl_seconds: Optional[int] = None, video: "raw.base.Document" = None) -> None:
        self.spoiler = spoiler
        self.live_photo = live_photo
        self.photo = photo
        self.ttl_seconds = ttl_seconds
        self.video = video

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaPhoto":
        
        flags = Int.read(b)
        
        spoiler = True if flags & (1 << 3) else False
        live_photo = True if flags & (1 << 4) else False
        photo = TLObject.read(b) if flags & (1 << 0) else None
        
        ttl_seconds = Int.read(b) if flags & (1 << 2) else None
        video = TLObject.read(b) if flags & (1 << 4) else None
        
        return MessageMediaPhoto(spoiler=spoiler, live_photo=live_photo, photo=photo, ttl_seconds=ttl_seconds, video=video)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.spoiler else 0
        flags |= (1 << 4) if self.live_photo else 0
        flags |= (1 << 0) if self.photo is not None else 0
        flags |= (1 << 2) if self.ttl_seconds is not None else 0
        flags |= (1 << 4) if self.video is not None else 0
        b.write(Int(flags))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))
        
        if self.video is not None:
            b.write(self.video.write())
        
        return b.getvalue()

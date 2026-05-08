
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMediaUploadedPhoto(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``7D8375DA``

    Parameters:
        file (:obj:`InputFile <pyrogram.raw.base.InputFile>`):
            N/A

        spoiler (``bool``, *optional*):
            N/A

        live_photo (``bool``, *optional*):
            N/A

        stickers (List of :obj:`InputDocument <pyrogram.raw.base.InputDocument>`, *optional*):
            N/A

        ttl_seconds (``int`` ``32-bit``, *optional*):
            N/A

        video (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["file", "spoiler", "live_photo", "stickers", "ttl_seconds", "video"]

    ID = 0x7d8375da
    QUALNAME = "types.InputMediaUploadedPhoto"

    def __init__(self, *, file: "raw.base.InputFile", spoiler: Optional[bool] = None, live_photo: Optional[bool] = None, stickers: Optional[List["raw.base.InputDocument"]] = None, ttl_seconds: Optional[int] = None, video: "raw.base.InputDocument" = None) -> None:
        self.file = file
        self.spoiler = spoiler
        self.live_photo = live_photo
        self.stickers = stickers
        self.ttl_seconds = ttl_seconds
        self.video = video

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaUploadedPhoto":
        
        flags = Int.read(b)
        
        spoiler = True if flags & (1 << 2) else False
        live_photo = True if flags & (1 << 3) else False
        file = TLObject.read(b)
        
        stickers = TLObject.read(b) if flags & (1 << 0) else []
        
        ttl_seconds = Int.read(b) if flags & (1 << 1) else None
        video = TLObject.read(b) if flags & (1 << 3) else None
        
        return InputMediaUploadedPhoto(file=file, spoiler=spoiler, live_photo=live_photo, stickers=stickers, ttl_seconds=ttl_seconds, video=video)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.spoiler else 0
        flags |= (1 << 3) if self.live_photo else 0
        flags |= (1 << 0) if self.stickers else 0
        flags |= (1 << 1) if self.ttl_seconds is not None else 0
        flags |= (1 << 3) if self.video is not None else 0
        b.write(Int(flags))
        
        b.write(self.file.write())
        
        if self.stickers is not None:
            b.write(Vector(self.stickers))
        
        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))
        
        if self.video is not None:
            b.write(self.video.write())
        
        return b.getvalue()

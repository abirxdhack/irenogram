
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMediaPhoto(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``E3AF4434``

    Parameters:
        id (:obj:`InputPhoto <pyrogram.raw.base.InputPhoto>`):
            N/A

        spoiler (``bool``, *optional*):
            N/A

        live_photo (``bool``, *optional*):
            N/A

        ttl_seconds (``int`` ``32-bit``, *optional*):
            N/A

        video (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "spoiler", "live_photo", "ttl_seconds", "video"]

    ID = 0xe3af4434
    QUALNAME = "types.InputMediaPhoto"

    def __init__(self, *, id: "raw.base.InputPhoto", spoiler: Optional[bool] = None, live_photo: Optional[bool] = None, ttl_seconds: Optional[int] = None, video: "raw.base.InputDocument" = None) -> None:
        self.id = id
        self.spoiler = spoiler
        self.live_photo = live_photo
        self.ttl_seconds = ttl_seconds
        self.video = video

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaPhoto":
        
        flags = Int.read(b)
        
        spoiler = True if flags & (1 << 1) else False
        live_photo = True if flags & (1 << 2) else False
        id = TLObject.read(b)
        
        ttl_seconds = Int.read(b) if flags & (1 << 0) else None
        video = TLObject.read(b) if flags & (1 << 2) else None
        
        return InputMediaPhoto(id=id, spoiler=spoiler, live_photo=live_photo, ttl_seconds=ttl_seconds, video=video)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.spoiler else 0
        flags |= (1 << 2) if self.live_photo else 0
        flags |= (1 << 0) if self.ttl_seconds is not None else 0
        flags |= (1 << 2) if self.video is not None else 0
        b.write(Int(flags))
        
        b.write(self.id.write())
        
        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))
        
        if self.video is not None:
            b.write(self.video.write())
        
        return b.getvalue()

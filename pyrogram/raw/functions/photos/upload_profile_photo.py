
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UploadProfilePhoto(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``388A3B5``

    Parameters:
        fallback (``bool``, *optional*):
            N/A

        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`, *optional*):
            N/A

        file (:obj:`InputFile <pyrogram.raw.base.InputFile>`, *optional*):
            N/A

        video (:obj:`InputFile <pyrogram.raw.base.InputFile>`, *optional*):
            N/A

        video_start_ts (``float`` ``64-bit``, *optional*):
            N/A

        video_emoji_markup (:obj:`VideoSize <pyrogram.raw.base.VideoSize>`, *optional*):
            N/A

    Returns:
        :obj:`photos.Photo <pyrogram.raw.base.photos.Photo>`
    """

    __slots__: List[str] = ["fallback", "bot", "file", "video", "video_start_ts", "video_emoji_markup"]

    ID = 0x388a3b5
    QUALNAME = "functions.photos.UploadProfilePhoto"

    def __init__(self, *, fallback: Optional[bool] = None, bot: "raw.base.InputUser" = None, file: "raw.base.InputFile" = None, video: "raw.base.InputFile" = None, video_start_ts: Optional[float] = None, video_emoji_markup: "raw.base.VideoSize" = None) -> None:
        self.fallback = fallback
        self.bot = bot
        self.file = file
        self.video = video
        self.video_start_ts = video_start_ts
        self.video_emoji_markup = video_emoji_markup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UploadProfilePhoto":
        
        flags = Int.read(b)
        
        fallback = True if flags & (1 << 3) else False
        bot = TLObject.read(b) if flags & (1 << 5) else None
        
        file = TLObject.read(b) if flags & (1 << 0) else None
        
        video = TLObject.read(b) if flags & (1 << 1) else None
        
        video_start_ts = Double.read(b) if flags & (1 << 2) else None
        video_emoji_markup = TLObject.read(b) if flags & (1 << 4) else None
        
        return UploadProfilePhoto(fallback=fallback, bot=bot, file=file, video=video, video_start_ts=video_start_ts, video_emoji_markup=video_emoji_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.fallback else 0
        flags |= (1 << 5) if self.bot is not None else 0
        flags |= (1 << 0) if self.file is not None else 0
        flags |= (1 << 1) if self.video is not None else 0
        flags |= (1 << 2) if self.video_start_ts is not None else 0
        flags |= (1 << 4) if self.video_emoji_markup is not None else 0
        b.write(Int(flags))
        
        if self.bot is not None:
            b.write(self.bot.write())
        
        if self.file is not None:
            b.write(self.file.write())
        
        if self.video is not None:
            b.write(self.video.write())
        
        if self.video_start_ts is not None:
            b.write(Double(self.video_start_ts))
        
        if self.video_emoji_markup is not None:
            b.write(self.video_emoji_markup.write())
        
        return b.getvalue()

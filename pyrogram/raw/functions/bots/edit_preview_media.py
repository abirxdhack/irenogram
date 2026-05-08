
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EditPreviewMedia(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``8525606F``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        lang_code (``str``):
            N/A

        media (:obj:`InputMedia <pyrogram.raw.base.InputMedia>`):
            N/A

        new_media (:obj:`InputMedia <pyrogram.raw.base.InputMedia>`):
            N/A

    Returns:
        :obj:`BotPreviewMedia <pyrogram.raw.base.BotPreviewMedia>`
    """

    __slots__: List[str] = ["bot", "lang_code", "media", "new_media"]

    ID = 0x8525606f
    QUALNAME = "functions.bots.EditPreviewMedia"

    def __init__(self, *, bot: "raw.base.InputUser", lang_code: str, media: "raw.base.InputMedia", new_media: "raw.base.InputMedia") -> None:
        self.bot = bot
        self.lang_code = lang_code
        self.media = media
        self.new_media = new_media

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditPreviewMedia":
        
        bot = TLObject.read(b)
        
        lang_code = String.read(b)
        
        media = TLObject.read(b)
        
        new_media = TLObject.read(b)
        
        return EditPreviewMedia(bot=bot, lang_code=lang_code, media=media, new_media=new_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.bot.write())
        
        b.write(String(self.lang_code))
        
        b.write(self.media.write())
        
        b.write(self.new_media.write())
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionChangeEmojiStickerSet(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``46D840AB``

    Parameters:
        prev_stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            N/A

        new_stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            N/A

    """

    __slots__: List[str] = ["prev_stickerset", "new_stickerset"]

    ID = 0x46d840ab
    QUALNAME = "types.ChannelAdminLogEventActionChangeEmojiStickerSet"

    def __init__(self, *, prev_stickerset: "raw.base.InputStickerSet", new_stickerset: "raw.base.InputStickerSet") -> None:
        self.prev_stickerset = prev_stickerset
        self.new_stickerset = new_stickerset

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangeEmojiStickerSet":
        
        prev_stickerset = TLObject.read(b)
        
        new_stickerset = TLObject.read(b)
        
        return ChannelAdminLogEventActionChangeEmojiStickerSet(prev_stickerset=prev_stickerset, new_stickerset=new_stickerset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.prev_stickerset.write())
        
        b.write(self.new_stickerset.write())
        
        return b.getvalue()


from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetEmojiStickers(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``3CD930B7``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "stickerset"]

    ID = 0x3cd930b7
    QUALNAME = "functions.channels.SetEmojiStickers"

    def __init__(self, *, channel: "raw.base.InputChannel", stickerset: "raw.base.InputStickerSet") -> None:
        self.channel = channel
        self.stickerset = stickerset

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetEmojiStickers":
        
        channel = TLObject.read(b)
        
        stickerset = TLObject.read(b)
        
        return SetEmojiStickers(channel=channel, stickerset=stickerset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        b.write(self.stickerset.write())
        
        return b.getvalue()
